import types
import weakref
from typing import Any, OrderedDict, Final


BUILTIN_COLLECTIONS: Final[frozenset[type[Any]]] = frozenset(
    {
        dict,
        list,
        set,
        tuple,
        frozenset,
        OrderedDict,
    }
)
IMMUTABLE_NON_COLLECTIONS: frozenset[type[Any]] = frozenset(
    {
        type(None),
        type(Ellipsis),
        type(NotImplemented),
        int,
        float,
        bool,
        complex,
        bytes,
        str,
        types.CodeType,
        type,
        range,
        types.BuiltinFunctionType,
        types.FunctionType,
        weakref.ref,
        property,
    }
)
IMMUTABLE_TYPES: Final[frozenset[type[Any]]] = frozenset(
    {
        *IMMUTABLE_NON_COLLECTIONS,
        tuple,
        frozenset,
        slice,
    }
)
BUILTIN_COPY: Final[frozenset[type[Any]]] = frozenset({bytearray, dict, list, set})
