def main():
    print('this is main')


def iter_improve(update, isclose, guess=1):
    while not isclose(guess):
        guess = update(guess)
    return guess

if __name__ == "__main__":
    main()
