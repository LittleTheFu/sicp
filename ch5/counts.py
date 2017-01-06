class Positives(object):

    def __init__(self):
        self.current = 0

    def __next__(self):
        result = self.current
        self.current += 1
        return result

    def __iter__(self):
        return self


def main():
    num = Positives()
    while True:
        print(num.__next__())

if __name__ == "__main__":
    main()
