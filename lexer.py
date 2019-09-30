from rply import LexerGenerator

#
# import re
# re.compile(r'\|\|')
#
from utils import log

lg = LexerGenerator()

# Keywords
lg.add('IF', r'if')
lg.add('ELSE', r'else')
lg.add('WHILE', r'while')
lg.add('FOR', r'for')
lg.add('VAR', r'var')
lg.add('FN', r'fn')
lg.add('RETURN', r'return')
lg.add('PRINT', r'print')

# todo add string literal
lg.add('NUMBER', r'\d+')
# todo add float literal
lg.add('ID', r'[a-zA-Z][a-zA-Z0-9]*')

# operators
lg.add('PLUS', r'\+')
lg.add('MINUS', r'-')
lg.add('MUL', r'\*')
lg.add('DIV', r'/')
lg.add('LT', r'<')
lg.add('GT', r'>')
lg.add('LE', r'<=')
lg.add('GE', r'>=')
lg.add('EQ', r'==')
lg.add('NE', r'!=')
lg.add('AND', r'&&')
lg.add('OR', r'\|\|')
lg.add('ASSIGN', r'=')
lg.add('COMMA', r'\,')
lg.add('DOT', r'\.')
lg.add('SEMI', r';')
lg.add('LPAREN', r'\(')
lg.add('RPAREN', r'\)')
lg.add('LBRACK', r'\[')
lg.add('RBRACK', r'\]')
lg.add('LBRACE', r'\{')
lg.add('RBRACE', r'\}')

# comment
lg.ignore('\s+')

lexer = lg.build()

if __name__ == '__main__':
    prog = 'var x = 1 + 1'
    for token in lexer.lex('var x = 1 + 1;'):
        log('prog: ', prog)
        log('token: ', token)
