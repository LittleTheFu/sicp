class Stream(object):

    def __init__(self, first, compute_rest, empty=False):
        self.first = first
        self._compute_rest = compute_rest
        self.empty = empty
        self._rest = None
        self._computed = False

    @property
    def rest(self):
        assert not self.empty
        if not self._computed:
            self._rest = self._compute_rest()
            self._computed = True
        return self._rest

    def __repr__(self):
        if self.empty:
            return '<empty stream>'
        return 'Stream({0}, <compute_rest>)'.format(repr(self.first))


Stream.empty = Stream(None, None, True)

# --------------------------------------


def map_stream(fn, s):
    if s.empty:
        return s

    def compute_rest():
        return map_stream(fn, s.rest)
    return Stream(fn(s.first), compute_rest)


def filter_stream(fn, s):
    if s.empty:
        return s

    def compute_rest():
        return filter_stream(fn, s.rest)
    if fn(s.first):
        return Stream(s.first, compute_rest)
    return compute_rest()


def truncate_stream(s, k):
    if s.empty or k == 0:
        return Stream.empty

    def compute_rest():
        return truncate_stream(s.rest, k - 1)
    return Stream(s.first, compute_rest)


def stream_to_list(s):
    r = []
    while not s.empty:
        r.append(s.first)
        s = s.rest
    return r


def make_integer_stream(first=1):
    def compute_rest():
        return make_integer_stream(first + 1)
    return Stream(first, compute_rest)


def main():
    print('-----------------')
    s = Stream(1, lambda: Stream(2, lambda: Stream.empty))
    print(s)
    print(s.first)
    print(s.rest)
    print(s.rest.first)
    print(s.rest.rest)
    print('-----------------\n')

    ints = make_integer_stream()
    print(ints)
    print(ints.first)
    print(ints.rest)
    print(ints.rest.rest.rest)
    print(ints.rest.rest.rest.first)
    print('-----------------\n')

    s = make_integer_stream(3)
    print(s)

    m = map_stream(lambda x: x * x, s)
    print(m)

    print(stream_to_list(truncate_stream(m, 5)))

if __name__ == "__main__":
    main()
