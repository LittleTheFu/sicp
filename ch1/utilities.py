def square(x):
    return x * x


def increment(x):
    return x + 1


def average(x, y):
    return (x + y) / 2


def approx_eq(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance


def near(x, f, g):
    return approx_eq(f(x), g(x))


def iter_improve(update, isclose, guess=1):
    while not isclose(guess):
        guess = update(guess)
    return guess
