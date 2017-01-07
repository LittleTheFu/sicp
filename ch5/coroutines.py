def match(pattern):
    print('Looking for ' + pattern)
    try:
        while True:
            s = (yield)
            if pattern in s:
                print(s)
    except GeneratorExit:
        print('===Done===')


def read(text, next_coroutine):
    for line in text.split():
        next_coroutine.send(line)
    next_coroutine.close()


def match_filter(pattern, next_coroutine):
    print('Looking for ' + pattern)
    try:
        while True:
            s = (yield)
            if pattern in s:
                next_coroutine.send(s)
    except GeneratorExit:
        next_coroutine.close()


def print_consumer():
    print('Preparing to print')
    try:
        while True:
            line = (yield)
            print(line)
    except GeneratorExit:
        print('===Done===')


def count_letters(next_coroutine):
    try:
        while True:
            s = (yield)
            counts = {letter: s.count(letter) for letter in set(s)}
            next_coroutine.send(counts)
    except GeneratorExit:
        next_coroutine.close()


def sum_dictionaries():
    total = {}
    try:
        while True:
            counts = (yield)
            for letter, count in counts.items():
                total[letter] = count + total.get(letter, 0)
    except GeneratorExit:
        max_letter = max(total.items(), key=lambda t: t[1])[0]
        print('Most frequent letter : ' + max_letter)


def read_to_many(text, coroutines):
    for word in text.split():
        for coroutine in coroutines:
            coroutine.send(word)
    for coroutine in coroutines:
        coroutine.close()


def main():
    print('===============')
    m = match('Jabberwock')
    m.__next__()
    m.send("the Jabberwock with eyes of flame")
    m.send("came whiffling through the tulgey wood")
    m.send("and burbled as it came")
    m.close()
    print('===============')

    text = 'Commending spending is offending to people pending lending!'
    matcher = match('ending')
    matcher.__next__()
    read(text, matcher)
    print('===============')

    printer = print_consumer()
    printer.__next__()
    match_f = match_filter('pend', printer)
    match_f.__next__()
    read(text, match_f)
    print('===============')

    s = sum_dictionaries()
    s.__next__()
    c = count_letters(s)
    c.__next__()
    read(text, c)
    print('===============')

    m1 = match('mend')
    m1.__next__()

    m2 = match('pe')
    m2.__next__()

    read_to_many(text, [m1, m2])

if __name__ == "__main__":
    main()
