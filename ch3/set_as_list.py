from recursive_list import Rlist, filter_rlist, extend_rlist


def empty(s):
    return s is Rlist.empty


def set_contains(s, v):
    if empty(s):
        return False
    if s.first == v:
        return True
    return set_contains(s.rest, v)


def adjoin_set(s, v):
    if set_contains(s, v):
        return s
    return Rlist(v, s)


def union_set(set1, set2):
    set1_not_set2 = filter_rlist(set1, lambda v: not set_contains(set2, v))
    return extend_rlist(set2, set1_not_set2)


def intersect_set(set1, set2):
    return filter_rlist(set1, lambda v: set_contains(set2, v))


# check ordered set
def intersect_set_by_order(set1, set2):
    if empty(set1) or empty(set2):
        return Rlist.empty
    e1, e2 = set1.first, set2.first
    if e1 == e2:
        return Rlist(e1, intersect_set_by_order(set1.rest, set2.rest))
    elif e1 < e2:
        return intersect_set_by_order(set1.rest, set2)
    elif e1 > e2:
        return intersect_set_by_order(set1, set2.rest)


def main():
    s = Rlist(1, Rlist(2, Rlist(3)))
    r = Rlist(1, Rlist(3, Rlist(8)))
    print('s : ', s)
    print('r : ', r)
    print(set_contains(s, 2))
    print(set_contains(s, 5))
    print(adjoin_set(s, 4))
    print(intersect_set(s, r))
    print(union_set(s, r))
    print('----------------------')

    a = Rlist(1, Rlist(2, Rlist(4, Rlist(8))))
    b = Rlist(1, Rlist(5, Rlist(7, Rlist(8))))
    print(intersect_set_by_order(a, b))


if __name__ == "__main__":
    main()
