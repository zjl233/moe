from rply import ParserGenerator
from rply.lexer import LexerStream

from src.ast import *

pg = ParserGenerator(
    # A list of all token names, accepted by the parser.
    tokens=['NUMBER', 'LPAREN', 'RPAREN',
            'PLUS', 'MINUS', 'MUL', 'DIV',
            'ID', 'ASSIGN', 'VAR', 'SEMI', 'PRINT'
            ],
    # A list of precedence rules with `ascending` precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV']),
        ('left', ['ASSIGN']),
    ]
)


# all lower case(expr...) is ast
# all upper case(NUMBER...) is token, and must be convert to ast before return

# this file(parser.py) only pass token to ast, thus don't preprocess token to str, int...
# like web framework, parser is controller and ast is service(maybe wrong, i need to read more book about compiler)

@pg.production("main : stmtlst")
def main(p) -> BaseBox:
    return p[0]


@pg.production('stmtlst : stmt')
def stmtlist_stmt(p: List[ASTNode]) -> Block:
    return Block.from_statement(p[0])


@pg.production('stmtlst : stmtlst stmt')
def stmtlist_stmtlist(p: List) -> Block:
    return p[0].append(p[1])


@pg.production('stmt : expr SEMI')
def stmt_expr(p: List) -> ASTNode:
    return p[0]


@pg.production('stmt : VAR ID ASSIGN expr SEMI')
def expr_assign(p):
    return Assignment(IdentifierReference(p[1].getstr()), p[3])


@pg.production('stmt : PRINT LPAREN expr RPAREN SEMI')
def stmt_expr(p: List) -> Print:
    return Print(p[2])


@pg.production('expr : NUMBER')
def expr_number(p: Tokens) -> Number:
    # p is a list of the pieces matched by the right hand side of the
    # rule
    return Number(p[0])


@pg.production('expr : LPAREN expr RPAREN')
def expr_parens(p):
    return p[1]


@pg.production('expr : expr PLUS expr')
@pg.production('expr : expr MINUS expr')
@pg.production('expr : expr MUL expr')
@pg.production('expr : expr DIV expr')
def expr_binop(p) -> BinaryOp:
    return BinaryOp(p[0], p[1], p[2])


@pg.production('expr : ID')
def expr_id(p: Tokens) -> IdentifierReference:
    return IdentifierReference(p[0].getstr())


parser = pg.build()


def parse(tokens: LexerStream) -> ASTNode:
    return parser.parse(tokens)
