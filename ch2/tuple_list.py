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


def make_mutable_rlist():
    contents = empty_rlist

    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_rlist(contents)
        elif message == 'getitem':
            return getitem_rlist(contents, value)
        elif message == 'push_first':
            contents = make_rlist(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return str(contents)
    return dispatch


def main():
    print('----------')
    counts = make_rlist(1, make_rlist(
        2, make_rlist(3, make_rlist(4, empty_rlist))))
    print(first(counts))
    print(rest(counts))
    print(len_rlist(counts))
    print(getitem_rlist(counts, 2))
    print('----------')
    another_list = make_mutable_rlist()
    print(another_list('len'))
    another_list('push_first', 1)
    another_list('push_first', 2)
    another_list('push_first', 3)
    print(another_list('str'))
    print(another_list('len'))
    print(another_list('getitem', 2))

if __name__ == "__main__":
    main()
