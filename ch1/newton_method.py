from utilities import iter_improve, approx_eq, square


def main():
    print(sqrt_root(3))
    print(sqrt_root(9))
    print(logarithm(27, 3))
    print(logarithm(1024, 2))
    print(logarithm(100, 4))
    pass


def approx_derivative(f, x, delta=1e-5):
    df = f(x + delta) - f(x)
    return df / delta


def newton_update(f):
    def update(x):
        return x - f(x) / approx_derivative(f, x)
    return update


def find_root(f, initial_guess=10):
    def test(x):
        return approx_eq(f(x), 0)
    return iter_improve(newton_update(f), test, initial_guess)


def sqrt_root(a):
    return find_root(lambda x: square(x) - a)


def logarithm(a, base=2):
    return find_root(lambda x: pow(base, x) - a)


if __name__ == "__main__":
    main()
