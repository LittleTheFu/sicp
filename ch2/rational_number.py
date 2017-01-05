from operator import getitem
from fractions import gcd


def make_rat(n, d):
    g = gcd(n, d)
    return (n // g, d // g)


def number(x):
    return getitem(x, 0)


def denom(x):
    return getitem(x, 1)


def str_rat(x):
    return '{0}/{1}'.format(number(x), denom(x))


def add_rat(x, y):
    nx, dx = number(x), denom(x)
    ny, dy = number(y), denom(y)
    return make_rat(nx * dy + ny * dx, dx * dy)


def mul_rat(x, y):
    return make_rat(number(x) * number(y), denom(x) * denom(y))


def eq_rat(x, y):
    return number(x) * denom(y) == number(y) * denom(x)


def main():
    half = make_rat(1, 2)
    print(str_rat(half))

    third = make_rat(1, 3)
    # print(str_rat(add_rat(third, third)))
    two_third = add_rat(third, third)
    print(str_rat(two_third))
    print('this is main')

if __name__ == "__main__":
    main()
