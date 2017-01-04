def main():
    triple(2)


def trace1(fn):
    def wrapper(x):
        print('->', fn, '(', x, ')')
        fn(x)
    return wrapper


@trace1
def triple(x):
    return 3 * x

if __name__ == "__main__":
    main()
