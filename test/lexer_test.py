from rply import Token

from lexer import lexer

if __name__ == '__main__':
    print(list(lexer.lex('var x = 1;')))
    assert list(lexer.lex('var x = 1;')) == [Token('VAR', 'var'), Token('ID', 'x'), Token('ASSIGN', '='),
                                             Token('NUMBER', '1'), Token('SEMI', ';')]
    print('all test passed')
