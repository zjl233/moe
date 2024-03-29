from src.lexer import lex
from src.parser import parse


# def repl():
#     while True:
#         try:
#             user_input = input('>> ').strip()
#         except EOFError:
#             break
#
#         if user_input:
#             tokens = lex(user_input)
#             tree = parse(tokens)
#             print(tree.eval({}))
#
#
# def test_print():
#     prog = 'print(6)'
#     tokens = lex(prog)
#     print(list(tokens))
#     tree = parse(tokens)
#     print(tree.eval({}))


def test_prog():
    prog = '''
    var y = 10;
    var x = 20;
    print(x + y);
    '''
    tokens = lex(prog)
    # print(list(tokens))
    tree = parse(tokens)
    print(type(tree))
    tree.eval({})


# def main(prog: str) -> None:
#     tokens = lex(prog)
#     tree = parse(tokens)


if __name__ == '__main__':
    test_prog()
    # repl()
