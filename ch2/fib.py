from operator import add
from functools import reduce


def fib(k):
    prev, curr = 1, 0
    for _ in range(k - 1):
        prev, curr = curr, prev + curr
    return curr


def is_even(n):
    return n % 2 == 0


def sum_even_fibs_1(n):
    return sum(filter(is_even, map(fib, range(1, n + 1))))


def sum_even_fibs_2(n):
    return sum(fib(k) for k in range(1, n + 1) if fib(k) % 2 == 0)


def sum_even_fibs_3(n):
    return reduce(add, filter(is_even, map(fib, range(1, n + 1))))


def main():
    print(sum_even_fibs_1(20))
    print(sum_even_fibs_2(20))
    print(sum_even_fibs_3(20))

if __name__ == "__main__":
    main()
