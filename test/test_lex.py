from unittest import TestCase


class TestLex(TestCase):
    def test_lex(self):
        from rply import Token

        from src.lexer import lex

        self.assertEqual(list(lex('var x = 1;')), [Token('VAR', 'var'), Token('ID', 'x'), Token('ASSIGN', '='),
                                                   Token('NUMBER', '1'), Token('SEMI', ';')])
        self.assertEqual(list(lex('10 10.1 0.1 233')), [Token('NUMBER', '10'), Token('NUMBER', '10.1'),
                                                        Token('NUMBER', '0.1'), Token('NUMBER', '233'), ])
