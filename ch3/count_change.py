def count_change(a, kinds=(50, 25, 10, 5, 1)):
    if a == 0:
        return 1
    elif a < 0 or len(kinds) == 0:
        return 0
    d = kinds[0]
    return count_change(a - d, kinds) + count_change(a, kinds[1:])


def main():
    print(count_change(100))

if __name__ == "__main__":
    main()
