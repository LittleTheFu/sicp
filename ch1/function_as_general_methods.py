from utilities import square, increment


def main():
    print(iter_improve(gold_update, gold_test))
    print((1 + pow(5, 1 / 2)) / 2)
    print('-------')
    print(square_root(2))
    print(square_root(3))
    print(square_root(9))


def average(x, y):
    return (x + y) / 2


def iter_improve(update, isclose, guess=1):
    while not isclose(guess):
        guess = update(guess)
    return guess


def approx_eq(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance


def near(x, f, g):
    return approx_eq(f(x), g(x))


# -----------------------
def gold_update(guess):
    return 1 / guess + 1


# solve the equation x^2-x-1=0
def gold_test(guess):
    return near(guess, square, increment)


# -----------------------
def square_root(x):
    def update(g):
        return average(g, x / g)

    def test(g):
        return approx_eq(x, square(g))

    return iter_improve(update, test)

if __name__ == "__main__":
    main()
