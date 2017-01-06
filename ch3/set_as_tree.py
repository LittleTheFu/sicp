from tree import Tree


def set_contains(s, v):
    if s is None:
        return False
    elif s.entry == v:
        return True
    elif s.entry < v:
        return set_contains(s.right, v)
    elif s.entry > v:
        return set_contains(s.left, v)


def adjoin_set(s, v):
    if s is None:
        return Tree(v)
    elif s.entry == v:
        return s
    elif s.entry < v:
        return Tree(s.entry, s.left, adjoin_set(s.right, v))
    elif s.entry > v:
        return Tree(s.entry, adjoin_set(s.left, v), s.right)


def main():
    s = adjoin_set(adjoin_set(adjoin_set(None, 2), 3), 1)
    print(s)
    print(set_contains(s, 1))
    print(set_contains(s, 10))

if __name__ == "__main__":
    main()
