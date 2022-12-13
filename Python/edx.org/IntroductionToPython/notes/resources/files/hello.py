def main():
    name = input("What's your name? ")
    hello(name)


def hello(name="World"):
    return f'Hello, {name}'


if __name__ == "__main__":
    main()