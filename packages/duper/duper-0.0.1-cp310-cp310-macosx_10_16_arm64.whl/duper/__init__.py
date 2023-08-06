# SPDX-FileCopyrightText: 2023-present Bobronium <appkiller16@gmail.com>
#
# SPDX-License-Identifier: MIT
import copy
from functools import partial
from typing import TypeVar, ParamSpec, Any, Callable, NoReturn

import mypy

from duper import _msg
from duper.constants import (
    IMMUTABLE_NON_COLLECTIONS,
    BUILTIN_COLLECTIONS,
    BUILTIN_COPY,
    IMMUTABLE_TYPES,
)
from duper.factories.ast import ast_factory
from duper.factories.runtime import (
    returns,
    get_reduce,
    debunk_reduce,
    reconstruct_copy,
)


T = TypeVar("T")
P = ParamSpec("P")


class Error(copy.Error):
    """
    Copy module can rise either copy.Error or any other exception that happens during copying
    Duper will do its best effort to always rise only duper.Error subclasses
    """


def warn(
    obj: T, memo: Any, factory: Callable[[T], Callable[[], T]], error: Exception
) -> Callable[[], T]:
    import warnings

    warnings.warn(
        f"\nCan't use {factory.__name__} to copy this {obj.__class__.__name__}: {error}"
        f"\nFalling back to builtin copy.deepcopy()"
        f"\nNote: such fallbacks may be slow, if they happen too often, consider using copy.deepcopy() directly",
        RuntimeWarning,
        stacklevel=3,
    )
    return partial(copy.deepcopy, obj, memo)


def fail(obj: T, _: Any, factory: Callable[[T], Callable[[], T]], error: Exception) -> NoReturn:
    __tracebackhide__ = True

    raise Error(
        f"Can't use `{_msg.repr(dup)}(..., factory={_msg.repr(factory)})` to copy this {_msg.repr(obj)}:"
        "\n" + " " * (len(_msg.repr(Error)) + 3) + f"{error!r}"
        f"\n\nTip: `{_msg.repr(dup)}(..., fallback={_msg.repr(warn)})` will fallback to standard deepcopy on errors"
    ) from error


def dup(
    obj: T,
    memo: Any = None,
    *,
    factory: Callable[[T], Callable[[], T]] = ast_factory,
    fallback: Callable[..., Callable[[], T]] = fail,
    check: bool = True,
) -> Callable[[], T]:
    """
    Finds the fastest way to repeatedly (deep)copy an object and returns copy factory
    """
    if memo != None:  # error: Local variable "memo" has inferred type None; add an annotation
        return fallback(
            obj,
            memo,
            factory,
            NotImplementedError("Usage of memo is not supported."),
        )
    cls: type[Any]
    if (cls := type(obj)) in IMMUTABLE_NON_COLLECTIONS or issubclass(cls, type):
        return partial(returns, obj)

    # special case for empty collections. should also work for empty tuples since they are constant
    if (builtin := cls in BUILTIN_COLLECTIONS) and not obj:
        return cls

    if not builtin:
        # seems like we can't speed things up here, unfortunately
        # being consistent with builtin deepcopy is better
        # than being just faster
        if (cp := getattr(obj, "__deepcopy__", None)) is not None:
            cp = cp({})
            return partial(cp.__deepcopy__, {})  # type: ignore
    else:
        if cls is dict:
            maybe_iterable = obj.values()  # type: ignore
        else:
            maybe_iterable = obj
        for v in maybe_iterable:  # type: ignore
            if v.__class__ not in IMMUTABLE_NON_COLLECTIONS:
                # looks like object is nested, we have to use deepcopy...
                #
                # could return factory here, but we have special logic when invoking
                # the factory that I didn't want to duplicate, nor abstract away
                #
                # note: this break prevents `else:` block after the loop to be executed
                break
        else:  # will be executed if all values inside a collection are immutable non-collections
            if cls in BUILTIN_COPY:  # faster than reconstructing
                return obj.copy().copy  # type: ignore

    try:
        compiled = factory(obj)
        if not check:
            return compiled
        try:
            compiled()
        except Exception as e:
            raise Error("Cannot reconstruct this object, see details above") from e
        return compiled
    except Exception as e:
        return fallback(obj, memo, factory, e)


def copier(obj: T) -> Callable[[], T]:
    """
    Finds the fastest way to repeatedly copy an object and returns copy factory
    """
    # handle two special cases when we don't
    if (cls := obj.__class__) in IMMUTABLE_TYPES or issubclass(cls, type):
        return partial(returns, obj)  # can just always return the same object

    if cls in BUILTIN_COLLECTIONS and not obj:
        return cls  # special case for empty collections

    if cls in BUILTIN_COPY:
        return obj.copy().copy  # type: ignore
    if cp := getattr(obj, "__copy__", None):
        return cp().__copy__

    rv = get_reduce(obj, cls)
    if isinstance(rv, str):
        return partial(returns, obj)

    func, args, kwargs, *rest = debunk_reduce(*rv)

    if any(r is not None for r in rest):
        return partial(reconstruct_copy, func, args, kwargs, *rest)

    return partial(func, *args, **kwargs)
