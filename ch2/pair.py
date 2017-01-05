def make_pair(x, y):
    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y

    return dispatch


def getitem_pair(p, i):
    return p(i)
