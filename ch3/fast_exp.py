def square(n):
    return n * n


def fast_exp(b, n):
    if n == 0:
        return 1
    if(n % 2 == 0):
        return square(fast_exp(b, n // 2))
    else:
        return b * fast_exp(b, n - 1)


def main():
    print(fast_exp(2, 100))

if __name__ == "__main__":
    main()
