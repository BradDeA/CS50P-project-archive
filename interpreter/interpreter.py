def main():
    a, b, c = input('Expression: ').split(' ')
    print(interpret(a,b,c))

def interpret(a,b,c):
    match b:
        case '+':
            return float(a) + float(c)
        case '-':
            return float(a) - float(c)
        case '*':
            return float(a) * float(c)
        case '/':
            return float(a) / float(c)
        case _:
            return 'Invalid'


main()