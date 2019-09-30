from rply import Token

from lexer import lexer

if __name__ == '__main__':
    assert list(lexer.lex('var x = 1;')) == [Token('VAR', 'var'), Token('ID', 'x'), Token('ASSIGN', '='),
                                             Token('NUMBER', '1'), Token('SEMI', ';')]
    assert list(lexer.lex('10 10.1 0.1 233')) == [Token('NUMBER', '10'), Token('NUMBER', '10.1'),
                                                  Token('NUMBER', '0.1'), Token('NUMBER', '233'), ]
    print('all test passed')
