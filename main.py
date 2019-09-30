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
    code = 'print(6)'
    tokens = lexer.lex(code)
    print(list(tokens))
    tree = parser.parse(tokens)
    print(tree.eval())


def test_code():
    code = '1 + 1 * 3'
    print(parser.parse(lexer.lex(code)).eval())


if __name__ == '__main__':
    test_code()
    # repl()
