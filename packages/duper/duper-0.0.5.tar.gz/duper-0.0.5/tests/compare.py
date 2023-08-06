import dataclasses
import types
import weakref
from copy import deepcopy
from copyreg import dispatch_table
from typing import Any
from typing import TypeVar

import duper


T = TypeVar("T")


@dataclasses.dataclass
class Context:
    memo: dict[int, Any] = dataclasses.field(default_factory=dict)
    diff: dict[int, Any] = dataclasses.field(default_factory=dict)

    def seen(self, x: T):
        if id(x) not in self.memo:
            self.memo[id(x)] = x
            return False
        return True

    def mismatch(self):
        self.diff.setdefault("", []).append(1)


def compare(x: T, first: T, second: T, context=None) -> None:
    if context is None:
        context = Context()

    compare_primitive(x, first, second, context)
    if context.seen(x):
        return context
    cls = type(x)

    comparator = compare_dispatch.get(cls)
    if comparator is not None:
        comparator(x, first, second, context)

    else:
        if issubclass(cls, type):
            return context
        copier = getattr(x, "__deepcopy__", None)
        if copier is not None:
            return context
        reductor = dispatch_table.get(cls)
        if not reductor:
            reductor = getattr(cls, "__reduce_ex__", None)
            if reductor:

                def reductor(o):
                    return cls.__reduce_ex__(o, 4)

        if not reductor:
            reductor = getattr(cls, "__reduce__", None)

        reduced = [[], [], [], [], []]
        for o in (x, first, second):
            rv = reductor(o)
            for i, v in enumerate(rv):
                reduced[i].append(rv)

        print(*reduced, sep="\n")
        compare_reduced(context, *reduced)
    return context


compare_dispatch = d = {}


def compare_primitive(x: T, first: T, second: T, context):
    try:
        equal = (x == first) == (x == second)
    except RecursionError:
        equal = True  # can't complain here

    if not (equal and (x is first) == (x is second)):
        context.mismatch()


d[type(None)] = compare_primitive
d[type(Ellipsis)] = compare_primitive
d[type(NotImplemented)] = compare_primitive
d[int] = compare_primitive
d[float] = compare_primitive
d[bool] = compare_primitive
d[complex] = compare_primitive
d[bytes] = compare_primitive
d[str] = compare_primitive
d[types.CodeType] = compare_primitive
d[type] = compare_primitive
d[types.BuiltinFunctionType] = compare_primitive
d[types.FunctionType] = compare_primitive
d[weakref.ref] = compare_primitive
d[property] = compare_primitive


def compare_iterable(x: T, first: T, second: T, memo: Context, compare=compare):
    memo.seen(x)
    for a, b, c in zip(x, first, second):
        compare(a, b, c, memo)


def compare_dict(x: T, first: T, second: T, memo, compare=compare):
    memo.seen(x)
    for (ak, av), (bk, bv), (ck, cv) in zip(x.items(), first.items(), second.items()):
        compare(ak, bk, ck, memo)
        compare(av, bv, cv, memo)


def compare_method(x: T, first: T, second: T, memo):  # Copy instance methods
    return type(x)(x.__func__, compare(x.__self__, first.__self__, second.__self__, memo))


d[types.MethodType] = compare_method

del d


def _keep_alive(x, memo):
    """Keeps a reference to the object x in the memo.

    Because we remember objects by their id, we have
    to assure that possibly temporary objects are kept
    alive by referencing them.
    We store a reference at the id of the memo, which should
    normally not be used unless someone tries to deepcopy
    the memo itself...
    """
    try:
        memo[id(memo)].append(x)
    except KeyError:
        # aha, this is the first one :-)
        memo[id(memo)] = [x]


def compare_reduced(
    memo,
    func,
    args,
    state=None,
    listiter=None,
    dictiter=None,
    compare=compare,
):
    if args:
        for arg in args:
            compare(*arg, context=memo)
    if state is not None:
        compare(*state, context=memo)
    if listiter is not None:
        for item in listiter:
            compare(*item, context=memo)
    if dictiter is not None:
        for key, value in dictiter:
            compare(*key, context=memo)
            compare(*value, context=memo)


def compared(x, first=deepcopy, second=duper.deepdupe):
    assert not compare(x, first(x), second(x)).diff


t = ([],)
t[0].append(t)

print(compared(t))
