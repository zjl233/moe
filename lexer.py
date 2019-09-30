from rply import LexerGenerator

#
# import re
# re.compile(r';')
#
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

# string liter
lg.add('NUMBER', r'\d+')
# float liter
lg.add('ID', r'[a-zA-Z][a-zA-Z0-9]*')

lg.add('PLUS', r'\+')
lg.add('MINUS', r'-')
lg.add('MUL', r'\*')
lg.add('DIV', r'/')
lg.add('LPAREN', r'\(')
lg.add('RPAREN', r'\)')
lg.add('LBRACK', r'\[')
lg.add('RBRACK', r'\]')
lg.add('LBRACE', r'\{')
lg.add('RBRACE', r'\}')
lg.add('ASSIGN', r'=')
lg.add('LT', r'<')
lg.add('GT', r'>')
lg.add('LE', r'<=')
lg.add('GE', r'>=')
lg.add('EQ', r'==')
lg.add('NE', r'!=')
lg.add('AND', r'&&')
lg.add('OR', r'||')
lg.add('SEMI', r';')
lg.add('COMMA', r'.')

# comment
lg.ignore('\s+')

lexer = lg.build()

if __name__ == '__main__':
    tokens = lexer.lex('1 + 1')
    print(list(tokens))