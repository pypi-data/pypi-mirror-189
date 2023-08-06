"""Runtime instructions to reproduce an object"""
import copyreg
from copy import Error

from typing import Any, Iterable, Callable

from duper import BUILTIN_COPY
from typing import TypeVar
from copyreg import __newobj_ex__, __newobj__  # type: ignore


T = TypeVar("T")


def returns(x: T) -> T:
    return x


def reconstruct_state(
    new_obj: T,
    state: Any = None,
    listiter: Iterable[Any] | None = None,
    dictiter: Iterable[tuple[Any, Any]] | None = None,
) -> T:
    if state is not None:
        if (setstate := getattr(new_obj, "__setstate__", None)) is not None:
            setstate(state)
        else:
            if isinstance(state, tuple) and len(state) == 2:
                state, slot_state = state
            else:
                slot_state = None

            if state is not None:
                new_obj.__dict__.update(state)
            if slot_state is not None:
                setattr_ = new_obj.__setattr__
                for key, value in slot_state.items():
                    setattr_(key, value)

    if listiter is not None:
        for item in listiter:
            new_obj.append(item)  # type: ignore
    if dictiter is not None:
        for key, value in dictiter:
            new_obj[key] = value  # type: ignore

    return new_obj


def reconstruct_copy(
    func: Callable[..., T],
    args: Any,
    kwargs: Any,
    state: Any = None,
    listiter: Iterable[Any] | None = None,
    dictiter: Iterable[tuple[Any, Any]] | None = None,
    *unsupported: Any,
) -> T:
    if unsupported:
        raise NotImplementedError(f"Unsupported reduce value length {5 + len(unsupported)}")
    reconstruct_state(new_obj := func(*args, **kwargs), state, listiter, dictiter)
    return new_obj


def get_reduce(
    x: Any, cls: type[Any]
) -> (
    str
    | tuple[Callable[..., Any], tuple[Any, ...]]
    | tuple[Callable[..., Any], tuple[Any, ...], Any]
    | tuple[Callable[..., Any], tuple[Any, ...], Any, Any, Any]
    | tuple[Callable[..., Any], tuple[Any, ...], Any, Any, Any, Any]
    | tuple[Any, ...]  # make sure we never fail on unexpected tuples
):
    if custom_reduce := copyreg.dispatch_table.get(cls):
        return custom_reduce(x)
    elif (__reduce_ex__ := getattr(x, "__reduce_ex__", None)) is not None:
        return __reduce_ex__(4)
    elif __reduce__ := getattr(x, "__reduce__", None):
        return __reduce__()
    else:
        raise Error(f"un(deep)copyable object of type {cls}")


def debunk_reduce(
    func: Callable[..., Any],
    args: tuple[Any, ...],
    state: Any = None,
    listiter: Iterable[Any] | None = None,
    dictiter: Iterable[tuple[Any, Any]] | None = None,
    *unsupported: Any,
) -> tuple[Any, ...]:
    if unsupported:
        raise NotImplementedError(f"Unexpected values in reduce value: {unsupported}")
    # __newobj__ and __newobj_ex__ are special wrapper functions
    # getting rid of them saves us from one extra call on stack
    if func is __newobj_ex__:
        cls, args, kwargs = args
        args = (cls, *args)
        func = cls.__new__
    elif func is __newobj__:
        func = args[0].__new__
        kwargs = {}
    else:
        kwargs = {}
    return func, args, kwargs, state, listiter, dictiter
