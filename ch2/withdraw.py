def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insuficient funds"
        balance = balance - amount
        return balance

    return withdraw


def main():
    wd = make_withdraw(100)
    print(wd(25))
    print(wd(25))
    print(wd(25))
    print(wd(35))


if __name__ == "__main__":
    main()
