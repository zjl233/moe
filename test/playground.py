import operator as op

op_map = {
    'PLUS': op.add,
    'MINUS': op.sub,
    'MUL': op.mul,
    'DIV': op.truediv,
}

print(('PLUS' in op_map))
print(op_map['PLUS'](1, 2))
l = ['first', 'second', 'third']
[first, second, third] = l
print(first)