def make_dict():
    records = []

    def getitem(key):
        for k, v in records:
            if k == key:
                return v

    def setitem(key, value):
        for item in records:
            if item[0] == key:
                item[1] = value
                return
        records.append([key, value])

    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            return setitem(key, value)
        elif message == 'keys':
            return tuple(k for k, _ in records)
        elif message == 'values':
            return tuple(v for _, v in records)
    return dispatch


def main():
    d = make_dict()
    d('setitem', 3, 9)
    d('setitem', 4, 16)
    print(d('getitem', 3))
    print(d('getitem', 4))
    print(d('keys'))
    print(d('values'))
    pass

if __name__ == "__main__":
    main()
