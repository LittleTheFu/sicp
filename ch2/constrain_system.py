from operator import add, sub, mul, truediv


def make_ternary_constraint(a, b, c, ab, cb, ca):
    def new_value():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))

    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)
    constraint = {'new_val': new_value, 'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint


def adder(a, b, c):
    return make_ternary_constraint(a, b, c, add, sub, sub)


def multiplier(a, b, c):
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)


def constant(connector, value):
    constraint = {}
    connector['set_val'](constraint, value)
    return constraint


def make_connector(name=None):
    informant = None
    constraints = []

    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('Contridiction detected:', val, 'vs', value)

    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgetten')
            inform_all_except(source, 'forget', constraints)

    connector = {'val': None, 'set_val': set_value, 'forget': forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source)}
    return connector


def inform_all_except(source, message, constrains):
    for c in constrains:
        if c != source:
            c[message]()


def make_converter(c, f):
    # global for debug output
    global u, v, w, x, y
    u, v, w, x, y = [make_connector() for _ in range(5)]

    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)


def debugPrint():
    print('!!!!!')
    for item in [u, v, w, x, y]:
        print(item['val'])
    print('!!!!!')


def main():
    celsius = make_connector('Celsius')
    fahreheit = make_connector('Fahreheit')
    make_converter(celsius, fahreheit)

    # debugPrint()
    fahreheit['set_val']('usr', 212)

    # debugPrint()
    fahreheit['forget']('usr')

    # debugPrint()
    celsius['set_val']('usr', 25)

    # debugPrint()

if __name__ == "__main__":
    main()
