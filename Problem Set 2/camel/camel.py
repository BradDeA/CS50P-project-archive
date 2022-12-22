def main():
    n = input('Variable Name: ')
    print(case(n))

def case(str):
    name = [str[0].lower()]
    for c in str[1:]:
        if c.isupper():
            name.append('_')
            name.append(c.lower())
        else:
            name.append(c)

    return ''.join(name)


main()