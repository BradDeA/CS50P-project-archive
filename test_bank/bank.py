def main():
    g = input('Greeting: ').strip(' ')
    print(value(g))


def value(greeting):
    g = greeting.lower()
    if f'{g}'.startswith('hello'):
        return 0
    if f'{g}'.startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()