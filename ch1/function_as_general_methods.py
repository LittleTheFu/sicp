def main():
    print(iter_improve(gold_update, gold_test))
    print((1 + pow(5, 1 / 2)) / 2)


def square(x):
    return x * x


def increment(x):
    return x + 1


def iter_improve(update, isclose, guess=1):
    while not isclose(guess):
        guess = update(guess)
    return guess


def approx_eq(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance


def near(x, f, g):
    return approx_eq(f(x), g(x))


def gold_update(guess):
    return 1 / guess + 1


# solve the equation x^2-x-1=0
def gold_test(guess):
    return near(guess, square, increment)

if __name__ == "__main__":
    main()
