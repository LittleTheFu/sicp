def make_instance(cls):
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value, instance)

    def set_value(name, value):
        attributes[name] = value

    attributes = {}
    instance = {'get': get_value, 'set': set_value}
    return instance


def bind_method(value, instance):
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value


def make_class(attributes, base_class=None):
    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)

    def set_value(name, value):
        attributes[name] = value

    def new(*args):
        return init_instance(cls, *args)

    cls = {'get': get_value, 'set': set_value, 'new': new}
    return cls


def init_instance(cls, *args):
    instance = make_instance(cls)
    init = cls['get']('__init__')
    if init:
        init(instance, *args)
    return instance

# -------------------------------------------------


def make_account_class():
    def __init__(self, account_holder):
        self['set']('holder', account_holder)
        self['set']('balance', 0)

    def desposit(self, amount):
        new_balance = self['get']('balance') + amount
        self['set']('balance', new_balance)
        return self['get']('balance')

    def withdraw(self, amount):
        balance = self['get']('balance')
        if amount > balance:
            return 'Insuficient funds'
        self['set']('balance', balance - amount)
        return self['get']('balance')
    return make_class({'__init__': __init__, 'desposit': desposit,
                       'withdraw': withdraw, 'interest': 0.02})


def main():
    Account = make_account_class()
    jim_account = Account['new']('Jim')

    print(jim_account['get']('holder'))
    print(jim_account['get']('interest'))

    print(jim_account['get']('desposit')(20))
    print(jim_account['get']('withdraw')(5))

    jim_account['set']('interest', 0.1)
    print(jim_account['get']('interest'))


if __name__ == "__main__":
    main()
