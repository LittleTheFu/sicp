from operator import mul
from functools import reduce


class Exp(object):

    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(self.operator, self.operands)

    def __str__(self):
        operands_str = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operands_str)


def calc_eval(exp):
    if type(exp) in (int, float):
        return exp
    elif type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)


def calc_apply(operator, args):
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer / denom


def read_eval_print_loop():
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):
            print('Calculation completed')
            return


def calc_parse(line):
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s) : ' + ' '.join(tokens))
    return expression_tree


def tokenize(line):
    spaced = line.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ')
    return spaced.strip().split()


def assert_not_empty(tokens):
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')

known_operators = ['add', 'sub', 'mul', 'div', '+', '-', '*', '/']


def analyze(tokens):
    assert_not_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (float, int):
        return token
    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expect ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    else:
        raise SyntaxError('unexpected ' + token)


def analyze_operands(tokens):
    assert_not_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected , ')
        operands.append(analyze(tokens))
        assert_not_empty(tokens)
    tokens.pop(0)
    return operands


def analyze_token(token):
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token


def main():
    # print(calc_apply('+', [1, 2, 3]))
    # e = Exp('add', [2, Exp('mul', [4, 6])])
    # print(e)
    # print(calc_eval(e))
    # print(tokenize('add(2, mul(4, 6))'))
    read_eval_print_loop()


if __name__ == "__main__":
    main()
