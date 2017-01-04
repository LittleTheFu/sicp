from utilities import increment


def sum_natures(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total


def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total


def sum_pi(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / (k * (k + 2)), k + 4
    return total
# -------------------------------------------


def summatition(n, term, next):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), next(k)
    return total


def cube(k):
    return pow(k, 3)


def pi_term(k):
    return 8 / (k * (k + 2))


def pi_next(k):
    return k + 4


def identity(k):
    return k

# -------------------------------------------


def sum_natures_better(n):
    return summatition(n, identity, increment)


def sum_cubes_better(n):
    return summatition(n, cube, increment)


def sum_pi_better(n):
    return summatition(n, pi_term, pi_next)


def main():
    print('-----')
    print('sum natures:')
    print(sum_natures(10000))
    print(sum_natures_better(10000))

    print('-----')
    print('sum cubes:')
    print(sum_cubes(10000))
    print(sum_cubes_better(10000))

    print('-----')
    print('sum pi:')
    print(sum_pi(10000))
    print(sum_pi_better(10000))

if __name__ == "__main__":
    main()
