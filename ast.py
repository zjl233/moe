import operator as op

from rply.token import BaseBox


class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value


class BinaryOp(BaseBox):
    op_map = {
        '+', op.add
    }

    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOp):
    def eval(self):
        return op.add(self.left.eval(), self.right.eval())


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Print(BaseBox):
    def __init__(self, expr) -> None:
        self.expr = expr

    def eval(self):
        print(self.expr.eval())
