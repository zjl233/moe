from lexer import lexer
from parser import parser


def repl():
    while True:
        try:
            user_input = input('>> ').strip()
        except EOFError:
            break

        if user_input:
            tokens = lexer.lex(user_input)
            tree = parser.parse(tokens)
            print(tree.eval())


def test_print():
    prog = 'print(6)'
    tokens = lexer.lex(prog)
    print(list(tokens))
    tree = parser.parse(tokens)
    print(tree.eval())


def test_prog():
    prog = '1 + 1 * 3'
    tokens = lexer.lex(prog)
    # print(list(tokens))
    tree = parser.parse(tokens)
    print(tree.eval())


def main(prog: str) -> None:
    tokens = lexer.lex(prog)
    tree = parser.parse(tokens)


if __name__ == '__main__':
    test_prog()
    # repl()
