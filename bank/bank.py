def main():
    g = input('Greeting: ').strip(' ')clear
    print(determine(g.lower()))

def determine(g):

    if f'{g}'.startswith('hello'):
        return '$0'
    if f'{g}'.startswith('h'):
        return '$20'
    else:
        return '$100'


main()