import operator as op

from rply.token import BaseBox, Token


class Number(BaseBox):
    def __init__(self, value: Token):
        self.value = int(value.getstr())

    def eval(self):
        return self.value

    def __repr__(self) -> str:
        return f'{self.__class__.__name__.lower()}<{self.value}>'


class BinaryOp(BaseBox):
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

    def eval(self):
        if self.opt not in self.op_map:
            raise NotImplementedError(self.opt, 'not supported')
        return self.op_map[self.opt](self.left.eval(), self.right.eval())


class Print(BaseBox):
    def __init__(self, expr) -> None:
        self.expr = expr

    def eval(self):
        print(self.expr.eval())
