from utilities import square, increment, average, approx_eq, near, iter_improve


def main():
    print(iter_improve(gold_update, gold_test))
    print((1 + pow(5, 1 / 2)) / 2)
    print('-------')
    print(square_root(2))
    print(square_root(3))
    print(square_root(9))


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
