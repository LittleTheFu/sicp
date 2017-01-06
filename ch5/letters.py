class Letters(object):

    def __init__(self):
        self.current = 'a'

    def __next__(self):
        if self.current > 'd':
            raise StopIteration
        result = self.current
        self.current = chr(ord(result) + 1)
        return result

    def __iter__(self):
        return self


class LetterIterable(object):

    def __iter__(self):
        current = 'a'
        while current <= 'd':
            yield current
            current = chr(ord(result) + 1)


def letters_generator():
    current = 'a'
    while current <= 'd':
        yield current
        current = chr(ord(current) + 1)


def all_pairs(s):
    for item1 in s:
        for item2 in s:
            yield (item1, item2)


def main():
    letters = Letters()
    print(letters.__next__())
    print(letters.__next__())
    print(letters.__next__())
    print(letters.__next__())
    # print(letters.__next__())
    print('----------------')

    letter_iter = letters_generator()
    print(letter_iter.__next__())
    print(letter_iter.__next__())
    print('----------------')

    for letter in letters_generator():
        print(letter)
    print('----------------')

    print(list(all_pairs([1, 2, 3])))
    print('----------------')

    lts = Letters()
    print(all_pairs(lts).__next__())
    print(all_pairs(lts).__next__())
    print('----------------')

    gen_letters = LetterIterable()
    print(all_pairs(gen_letters).__next__())
    print(all_pairs(gen_letters).__next__())
    print('----------------')


if __name__ == "__main__":
    main()
