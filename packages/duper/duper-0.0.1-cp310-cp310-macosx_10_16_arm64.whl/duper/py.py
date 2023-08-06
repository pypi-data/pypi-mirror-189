from _ast import AST, expr


class DummyStatement(expr):
    """Dummy class that we can give any form in place"""
    __class__: type[AST]
