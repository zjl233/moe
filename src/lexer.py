from rply import LexerGenerator
from rply.lexer import LexerStream

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

# Literals
lg.add('STRING', r'"(""|[^"])*"')
lg.add('NUMBER', r'-?\d+(\.\d+)?')
lg.add('ID', r'[a-zA-Z][a-zA-Z0-9]*')

# Operators
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

# Separators
lg.add('COMMA', r'\,')
lg.add('DOT', r'\.')
lg.add('SEMI', r';')
lg.add('LPAREN', r'\(')
lg.add('RPAREN', r'\)')
lg.add('LBRACK', r'\[')
lg.add('RBRACK', r'\]')
lg.add('LBRACE', r'\{')
lg.add('RBRACE', r'\}')

# whitespace and comment
lg.ignore(r'\s+')
lg.ignore(r"^#.*?")

lexer = lg.build()

token_names = [rule.name for rule in lg.rules]


def lex(prog: str) -> LexerStream:
    return lexer.lex(prog)
