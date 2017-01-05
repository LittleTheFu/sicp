empty_rlist = None


def make_rlist(first, rest):
    return (first, rest)


def first(s):
    return s[0]


def rest(s):
    return s[1]


def len_rlist(s):
    length = 0
    while(s != empty_rlist):
        s, length = rest(s), length + 1
    return length


def getitem_rlist(s, i):
    while(i > 0):
        s, i = rest(s), i - 1
    return first(s)


def main():
    counts = make_rlist(1, make_rlist(
        2, make_rlist(3, make_rlist(4, empty_rlist))))
    print(first(counts))
    print(rest(counts))
    print(len_rlist(counts))
    print(getitem_rlist(counts, 2))

if __name__ == "__main__":
    main()
