from __future__ import annotations

import operator as op
from typing import Dict, Optional, List

from rply.token import BaseBox, Token


class ASTNode(BaseBox):
    def eval(self, context: Context) -> Optional[ASTNode]:
        raise NotImplementedError(self.__class__)


Context = Dict[str, ASTNode]  # type alias
Tokens = List[Token]


class Block(ASTNode):
    def __init__(self, statements: List[ASTNode]) -> None:
        self.statements = statements

    @staticmethod
    def from_statement(statement: ASTNode) -> Block:
        return Block([statement])

    def extend(self, other: Block) -> Block:
        assert isinstance(other, Block)
        self.statements.extend(other.statements)
        return self

    def append(self, statement: ASTNode) -> Block:
        self.statements.append(statement)
        return self

    def eval(self, context: Context) -> None:
        for statement in self.statements:
            statement.eval(context)


class IdentifierReference(ASTNode):
    def __init__(self, name: str) -> None:
        self.name = name

    def eval(self, context: Context) -> Optional[ASTNode]:
        return context[self.name]


class Number(ASTNode):
    def __init__(self, value: Token):
        self.value = int(value.getstr())

    def eval(self, context: Context) -> Number:
        return self.value

    def __repr__(self) -> str:
        return f'{self.__class__.__name__.lower()}<{self.value}>'


class Assignment(ASTNode):
    def __init__(self, identifier: IdentifierReference, value: ASTNode) -> None:
        self.identifier = identifier
        self.value = value

    def eval(self, context: Context) -> None:
        value = self.value.eval(context)
        if value is None:
            raise AssertionError("Attempting to assign a null value")
        context[self.identifier.name] = value


class BinaryOp(ASTNode):
    op_map = {
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': op.truediv,
    }

    def __init__(self, left, opt: Token, right):
        self.left = left
        self.opt = opt.getstr()
        self.right = right

    def eval(self, context: Context) -> Optional[ASTNode]:
        if self.opt not in self.op_map:
            raise NotImplementedError(self.opt, 'not supported')

        return self.op_map[self.opt](self.left.eval(context), self.right.eval(context))


class Print(ASTNode):
    def __init__(self, expr: ASTNode) -> None:
        self.expr = expr

    def eval(self, context: Context) -> None:
        # print(self.expr.eval(context))
        print(self.expr.eval(context))
