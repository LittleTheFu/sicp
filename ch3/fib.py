def memo(f):
    cache = {}

    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorized


@memo
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n - 2) + fib(n - 1)


def main():
    print(fib(36))

if __name__ == "__main__":
    main()
