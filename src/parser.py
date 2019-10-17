from typing import List

from rply import ParserGenerator
from rply.lexer import LexerStream

from src.ast import *
from src.utils import dump_args

pg = ParserGenerator(
    # A list of all token names, accepted by the parser.
    tokens=['NUMBER', 'LPAREN', 'RPAREN',
            'PLUS', 'MINUS', 'MUL', 'DIV',
            'ID', 'ASSIGN', 'VAR'
            ],
    # A list of precedence rules with `ascending` precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV']),
        ('left', ['ASSIGN']),
    ]
)

memory = {}


# all lower case(expr...) is ast
# all upper case(NUMBER...) is token, and must be convert to ast before return


@pg.production("main : expr")
def main(p) -> BaseBox:
    return p[0]


@pg.production('expr : NUMBER')
@dump_args
def expr_number(p: List[Token]) -> Number:
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
@dump_args
def expr_binop(p) -> BinaryOp:
    return BinaryOp(p[0], p[1], p[2])


@pg.production('expr : VAR ID ASSIGN expr')
def expr_assign(p):
    # _, _id, _, expr = p
    print('enter assign')
    memory[p[1].getstr()] = p[3]
    return p[3]


@pg.production('expr : ID')
def expr_id(p):
    print(memory)
    print('enter id')
    return memory[p[0].getstr()]


# # todo implement print
# @pg.production('expr : PRINT LPAREN NUMBER RPAREN')
# def expr_print(p):
#     print(p)
#     print('enter print')
#     return Number(int(p[2].getstr()))


parser = pg.build()


def parse(tokens: LexerStream):
    return parser.parse(tokens)
