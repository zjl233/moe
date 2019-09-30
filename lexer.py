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
lg.add('DEF', r'def')
lg.add('PRINT', r'print')

lg.add('NUMBER', r'\d+')
lg.add('PLUS', r'\+')
lg.add('MINUS', r'-')
lg.add('MUL', r'\*')
lg.add('DIV', r'/')
lg.add('OPEN_PAREN', r'\(')
lg.add('CLOSE_PAREN', r'\)')
lg.add('OPEN_BRACE', r'\{')
lg.add('CLOSE_BRACE', r'\}')
lg.add('ASSIGN', r'=')
lg.add('LESS_THAN', r'<')
lg.add('MORE_THAN', r'>')
lg.add('LESS_THAN_EQUALS', r'<=')
lg.add('GREATER_THAN_EQUALS', r'>=')
lg.add('EQUALS', r'==')
lg.add('NOT_EQUALS', r'!=')
lg.add('AND', r'&&')
lg.add('OR', r'||')
lg.add('SEMICOLON', r';')


lg.add('ID', r'[a-zA-Z][a-zA-Z0-9]*')
lg.ignore('\s+')

lexer = lg.build()
