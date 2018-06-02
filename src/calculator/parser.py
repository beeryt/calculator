# calc.py - # A simple calculator without using eval
# A shorter and simpler re-implementation of http://www.dabeaz.com/ply/example.html

import operator as op
from plyplus import Grammar, STransformer

calc_grammar = Grammar("""
    start: expression;
    expression: add;
    ?add: (add add_symbol)? mul;
    ?mul: (mul mul_symbol)? term;
    @term: negate | number | '\(' expression '\)';
    negate: '-' term;

    number: '[\d.]+';
    mul_symbol: '\*' | '/' | '%';
    add_symbol: '\+' | '-';
    WHITESPACE: '[ \t]+' (%ignore);
""")

class Calc(STransformer):

    def _bin_operator(self, exp):
        arg1, operator_symbol, arg2 = exp.tail

        operator_func = { '+': op.add,
        				  '-': op.sub,
        				  '%': op.mod,
        				  '*': op.mul,
        				  '/': op.truediv }[operator_symbol]

        print(exp.tail, '=>', operator_func(arg1, arg2))
        return operator_func(arg1, arg2)

    number      = lambda self, exp: float(exp.tail[0])
    negate      = lambda self, exp: -exp.tail[0]
    __default__ = lambda self, exp: exp.tail[0]

    add = _bin_operator
    mul = _bin_operator

def main():
    calc = Calc()
    while True:
        try:
            s = input('> ')
        except EOFError:
        	break
        if s == '':
            break
        tree = calc_grammar.parse(s)
        print(tree.pretty())
        print(calc.transform(tree))

main()