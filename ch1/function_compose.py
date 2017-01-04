from utilities import square, increment


def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

add_one_and_square = compose1(square, increment)


def main():
    print(add_one_and_square(12))

if __name__ == "__main__":
    main()
