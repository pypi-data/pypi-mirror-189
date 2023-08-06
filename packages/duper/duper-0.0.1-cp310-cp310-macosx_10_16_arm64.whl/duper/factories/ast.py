"""
Construct AST that creates a deep copy of a given object
"""
import ast
import linecache
import pickle
import types
from _ast import (
    Load,
    Call,
    Name,
    Constant,
    List,
    Dict,
    Set,
    Tuple,
    AST,
    Return,
    FunctionDef,
    arguments,
    Module,
    stmt,
    keyword,
    Store,
    NamedExpr,
    expr,
)
from threading import Lock
from types import FunctionType
from typing import Any, NoReturn, Callable, TypeVar, Iterable, Final
from copyreg import __newobj_ex__, __newobj__  # type: ignore

# import astpretty

from duper.constants import IMMUTABLE_NON_COLLECTIONS, IMMUTABLE_TYPES
from duper.factories.runtime import reconstruct_state, get_reduce, debunk_reduce


T = TypeVar("T")

_d_setitem = dict.__setitem__


# default locations that ast sets in ast.fix_missing_locations()
# we can save a lot of time by setting them ourselves

LOAD = Load()
STORE = Store()
_locations = dict(lineno=1, col_offset=0, end_lineno=1, end_col_offset=0)

_nil: Final = expr()


def __loader__() -> None:
    """Special method to tell inspect that this file has special logic for loading code"""
    raise


def _get_name(value: Any) -> str:
    name = getattr(value, "__name__", "") or value.__class__.__name__
    if name in globals():
        return name
    return f"{name}_{id(value)}"


class DummyStatement(expr):
    def __init__(self) -> None:
        self.__dict__ = {}


class Namespace(dict):
    def load(self, value: Any, default: expr = _nil) -> expr:
        if (existing_statement := self.get(vid := id(value), _nil)) is not _nil:
            # if self.get(existing_statement, _nil) is _nil:
            #     raise RuntimeError(
            #         f"Shouldn't end up here: {existing_statement} should have been stored if its value id is stored"
            #     )

            # aha, we've seen this object already. we need to change its statement
            # to save its value in locals() via NamedExpr, before executing this code
            name = _get_name(value)
            if not isinstance(existing_statement, NamedExpr):
                # updating existing statement to assign itself to locals()
                # caller code should check if it's statement was updated
                # FIXME: kind of obscure, need to make this more obvious
                named_expr = self[existing_statement] = self[id(value)] = update_namespace(
                    name, existing_statement
                )
                if existing_statement is not ...:
                    new_statement = DummyStatement()
                    named_expr.value = new_statement
                    new_statement.__dict__.update(__class__=existing_statement.__class__)
                    new_statement.__dict__.update(existing_statement.__class__.__dict__)
                    new_statement.__dict__.update(existing_statement.__dict__)
                    existing_statement.__class__ = NamedExpr
                    existing_statement.__dict__.update(**named_expr.__class__.__dict__)
                    existing_statement.__dict__.update(named_expr.__dict__)

            # instead of regenerating current value, load it from namespace
            return get_from_namespace(name)
        return default

    def add(self, x: Any) -> str:
        self[vid := id(x)] = x
        self[name := _get_name(x)] = x
        return name

    def store(self, x: T) -> Name:
        """
        Stores object as is to be available in namespace
        """
        if id(x) in self:
            raise RuntimeError("Trying to store existing value?")
        self[name := _get_name(x)] = x
        return Name(id=name, ctx=LOAD, **_locations)

    def fix_references(self, elements: list[expr]) -> None:
        for i, e in enumerate(elements):
            if (new_e := self.get(e)) is not None:
                elements[i] = new_e

    def remember(self, x: Any, statement: T) -> T:
        # TODO: enforce type annotations
        if (existing_statement := self.get(vid := id(x), _nil)) not in {_nil, ...}:
            existing_statement.value = statement
            return existing_statement
        # statement = get_from_namespace(_get_name(x))
        self[vid] = statement
        return statement

    def update(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError("Use add instead")


def reconstruct_from_reduce(
    x: T,
    namespace: Namespace,
    func: Callable[..., T],
    args: Any,
    kwargs: Any,
    state: Any = None,
    listiter: Iterable[Any] | None = None,
    dictiter: Iterable[tuple[Any, Any]] | None = None,
) -> Call:
    if state is None and listiter is None and dictiter is None:
        return Call(
            func=namespace.store(func),
            args=[reconstruct_statement(item, namespace) for item in args],
            keywords=[
                keyword(
                    arg=name,
                    value=reconstruct_statement(item, namespace),
                    **_locations,
                )
                for name, item in kwargs.items()
            ],
            **_locations,
        )
    return Call(
        func=namespace.store(reconstruct_state),
        args=[
            NamedExpr(
                target=Name(
                    id=_get_name(x),
                    ctx=STORE,
                    **_locations,
                ),
                value=Call(
                    func=namespace.store(func),
                    args=[reconstruct_statement(item, namespace) for item in args],
                    keywords=[
                        keyword(
                            arg=name,
                            value=reconstruct_statement(item, namespace),
                            **_locations,
                        )
                        for name, item in kwargs.items()
                    ],
                    **_locations,
                ),
                **_locations,
            ),
            reconstruct_statement(state, namespace),
            Call(
                func=reconstruct_const(iter, namespace),
                args=[
                    reconstruct_list(
                        list(listiter) if listiter else [],
                        namespace,
                    )
                ],
                keywords=[],
                **_locations,
            ),
            Call(
                func=reconstruct_const(dict.items, namespace),
                args=[
                    reconstruct_dict(
                        dict(dictiter) if dictiter else {},
                        namespace,
                    )
                ],
                keywords=[],
                **_locations,
            ),
        ],
        keywords=[],
        **_locations,
    )


def reconstruct_const(x: Any, namespace: Namespace) -> Name | Constant:
    return (
        # can't use Constant with types in ast (which makes sense, there's no literals for them)
        # it's possible to substitute LOAD_GLOBAL with LOAD_CONST later in the bytecode,
        # but it's quite slow (with libs from PyPi), and doesn't give a big performance uplift
        # later, so I'm ignoring this for now
        namespace.store(x)
        if type(x) not in IMMUTABLE_TYPES
        or isinstance(
            x,
            (
                type,
                types.MethodType,
                types.BuiltinMethodType,
                types.FunctionType,
                types.MethodDescriptorType,
            ),
        )
        else Constant(value=x, **_locations)
    )


LT = TypeVar("LT", bound=list[Any])


def extend_list(x: LT, items: list[Any]) -> LT:
    x.extend(items)
    return x


def updates(function: Callable[..., T], x: T, args: Any) -> T:
    # list.append(x, args[0][0])
    # print()
    # print(f'{args=}')
    # print(f'{args[0]=}')
    # print(f'{args[0][0]=}')
    # print(f'{args[0][0]=}')
    # print(f'{(args[0][0],)=}')
    #
    # print(f"{x=}")
    function(x, args)
    # print(f"{x=}")
    # assert x is not x[0]
    # assert x is x[0][0]
    # assert len(x[0]) == 1, len(x[0])
    # assert len(x) == 1
    return x


def reconstruct_list(x: list[Any], namespace: Namespace) -> expr:
    list_literal = namespace.remember(x, List(**_locations, elts=[], ctx=LOAD))
    elts = [reconstruct_statement(i, namespace) for i in x]
    namespace.fix_references(elts)
    if (namespace_assignment := namespace[id(x)]) is list_literal:
        # list wasn't referenced inside itself, can reconstruct with literal
        list_literal.elts = elts  # type: ignore  # we're pretty sure that it's still a list :)
        return list_literal

    return Call(
        func=namespace.store(updates),
        args=[
            namespace.store(list.extend),
            namespace_assignment,
            Tuple(elts=elts, **_locations, ctx=LOAD),
        ],
        keywords=[],
        **_locations,
    )


DT = TypeVar("DT", bound=dict[Any, Any])


def update_dict(x: DT, keys: tuple[Any, ...], values: tuple[Any, ...]) -> DT:
    # relying on a caller to supply equal length keys and values
    x.update((k, v) for k, v in zip(keys, values))
    return x


def reconstruct_dict(x: dict[Any, Any], namespace: Namespace) -> Dict | Call:
    dict_literal = namespace.remember(x, Dict(keys=[], values=[], **_locations))
    keys = [reconstruct_statement(i, namespace) for i in x.keys()]
    values = [reconstruct_statement(i, namespace) for i in x.values()]

    if (dict_assignment := namespace[id(x)]) is dict_literal:
        # list wasn't referenced inside itself, can reconstruct with literal
        dict_literal.keys = keys  # type: ignore  # we're pretty sure that it's still a list :)
        dict_literal.values = values  # type: ignore  # we're pretty sure that it's still a list :)
        return dict_literal

    # x = {"foo": "bar"}
    # x["x"] = x
    # print(x)  # {"foo": "bar", "x": {...}}
    # print(ast.unparse(reconstruct_dict(x, Namespace())))  # update_dict(x := {"foo": "bar"}, ["x"], [x])
    return Call(
        func=namespace.store(update_dict),
        args=[
            dict_assignment,
            Tuple(elts=keys, **_locations, ctx=LOAD),
            Tuple(elts=values, **_locations, ctx=LOAD),
        ],
        keywords=[],
        **_locations,
    )


def reconstruct_set(x: set[Any], namespace: Namespace) -> Set | NamedExpr | Call:
    # FIXME: lots of duplicated logic from list
    set_literal = namespace.remember(x, Set(**_locations, elts=[], ctx=LOAD))
    elts = [reconstruct_statement(i, namespace) for i in x]
    namespace.fix_references(elts)
    if (namespace_assignment := namespace[id(x)]) is set_literal:
        # list wasn't referenced inside itself, can reconstruct with literal
        set_literal.elts = elts  # type: ignore  # we're pretty sure that it's still a list :)
        return set_literal

    return Call(
        func=namespace.store(updates),
        args=[
            namespace.store(set.update),
            namespace_assignment,
            Tuple(elts=elts, **_locations, ctx=LOAD),
        ],
        keywords=[],
        **_locations,
    )


CONSTANT_TYPES: Final = {Name, Constant}


def reconstruct_tuple(
    x: tuple[Any, ...] | frozenset[Any], namespace: Namespace
) -> Tuple | NamedExpr | Name | Constant:
    # FIXME: doesn't work with recursive structures
    immutable = True
    namespace.remember(x, ...)
    values = [
        statement
        for i in x
        if (  # this is a tuple of two expressions, always results in True
            # constructing list with list comprehension should be faster
            # than appending values, but we need to check each one individually as well,
            # so we're doing it with Lennon's (or Paul's?) operator.
            (statement := reconstruct_statement(i, namespace)),
            (
                immutable := immutable
                and (
                    (st := type(statement) is Constant)  # constant types ∫are immutable
                    or st is Name
                    and namespace[statement.id] is i  # True for types and functions
                )
            ),
        )
    ]
    if namespace.get(id(x)) is not ...:
        raise NotImplementedError("Self-referencing tuples and frozensets are not supported yet")

    if immutable:
        return reconstruct_const(x, namespace)

    namespace.fix_references(values)
    # deepcopy doesn't seem to put tuples in memo anywhere
    # but still checks if they are in memo
    # need to dig deeper to understand why and how they can end up there
    # one possible explanation: it was put in memo before deepcopy was called
    # if (remembered := namespace.get(tuple_expression)) is not _nil:
    #     return remembered
    # if more frozen types will be introduced, this should be a hashmap
    return Tuple(elts=values, ctx=LOAD, **_locations)


def reconstruct_method_deep(x: types.MethodType, namespace: Namespace) -> Call:
    return Call(
        func=reconstruct_const(x.__class__, namespace),
        args=[
            reconstruct_const(x.__func__, namespace),
            reconstruct_statement(x.__self__, namespace),
        ],
        keywords=[],
        **_locations,
    )


def update_namespace(name: str, value: expr) -> NamedExpr:
    return NamedExpr(
        target=Name(
            id=name,
            ctx=STORE,
            **_locations,
        ),
        value=value,
        **_locations,
    )


def get_from_namespace(name: str) -> Name:
    return Name(name, ctx=LOAD, **_locations)
    # above code should work
    #     func=Attribute(
    #         value=Call(
    #             func=Name(id="locals", ctx=LOAD, **_locations),
    #             args=[],
    #             keywords=[],
    #             **_locations,
    #         ),
    #         attr="__getitem__",
    #         ctx=Load(),
    #         **_locations,
    #     ),
    #     args=[
    #         Constant(
    #             value=name,
    #             kind=None,
    #             **_locations,
    #         ),
    #     ],
    #     keywords=[],
    #     **_locations,
    # )


def reconstruct_statement(x: Any, namespace: Namespace) -> expr:
    """
    Based on copy._reconstruct
    """

    cls = x.__class__
    if issubclass(cls, type) or cls in IMMUTABLE_NON_COLLECTIONS:
        return reconstruct_const(x, namespace)

    if (existing := namespace.load(x)) is not _nil:
        return existing

    constructor: Callable[[Any, Namespace], expr] | None = optimized_constructors.get(cls)

    if constructor is not None:
        return constructor(x, namespace)

    if (custom_copier := getattr(x, "__deepcopy__", None)) is not None:
        return reconstruct_from_reduce(x, namespace, custom_copier, ({},), {}, None, None, None)

    rv = get_reduce(x, cls)
    if isinstance(rv, str):  # global name
        return reconstruct_const(x, namespace)
    rv = debunk_reduce(*rv)

    if id(x) in namespace:
        return get_from_namespace(_get_name(x))
    namespace.remember(x, ...)
    return namespace.remember(x, reconstruct_from_reduce(x, namespace, *rv))


def ast_factory(x: T) -> Callable[[], T]:
    return_value_ast = reconstruct_statement(x, namespace := Namespace())
    return compile_function(
        f"produce_{x.__class__.__name__}",
        [Return(value=return_value_ast, **_locations)],
        namespace,
    )


optimized_constructors: dict[type[Any], Callable[[Any, Namespace], expr]] = {
    dict: reconstruct_dict,
    list: reconstruct_list,
    set: reconstruct_set,
    tuple: reconstruct_tuple,
    frozenset: reconstruct_tuple,
    types.ModuleType: reconstruct_const,
    types.MethodType: reconstruct_method_deep,
    **{t: reconstruct_const for t in IMMUTABLE_NON_COLLECTIONS},
}
FUNCTION = FunctionDef(
    name="FN",
    args=arguments(
        posonlyargs=[],
        args=[],
        vararg=None,
        kwonlyargs=[],
        kw_defaults=[],
        kwarg=None,
        defaults=[],
        **_locations,
    ),
    body=[],
    decorator_list=[],
    returns=None,
    type_comment=None,
    **_locations,
)
MODULE = Module(
    body=[FUNCTION],
    type_ignores=[],
    **_locations,
)

with_source = False


def compile_function(name: str, body: list[stmt], namespace: Namespace) -> FunctionType:
    global MODULE, FUNCTION
    with Lock():
        # changing variables on predefined AST is much faster
        # than constructing AST from scratch
        # locking just in case this is used in different threads
        FUNCTION.name = name
        FUNCTION.body = body
        if with_source:
            # oh, we can even construct accurate return type... wow, so much possibilities
            # TODO: specify used global names as well (custom types, etc.)
            assert len(body) == 1, "Initial implementation always contained 1 line of code"
            assert isinstance(body[0], Return)
            assert body[0].value is not None

            return_value = ast.unparse(body[0].value)
            source = [name := f"lambda: {return_value}"]
            FUNCTION.name = name
            file = f"<duper {hash(return_value)}>"
            linecache.cache[file] = (
                0,
                None,
                source,
                "",
            )
        else:
            file = "<duper factory (enable introspection to see source code)>"
        # astpretty.pprint(MODULE)
        # print(ast.unparse(MODULE))
        # ast.fix_missing_locations(MODULE)
        code = compile(MODULE, file, "exec")

    full_ns = {**globals(), **namespace}
    exec(code, full_ns)
    # namespace = dict(namespace)
    function = full_ns[name]
    function.__module__ = __name__
    return function
