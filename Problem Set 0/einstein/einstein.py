def main():
    mass = int(input('m: '))
    joules = equation(mass)
    print(joules)

def equation(mass):
    return mass * pow(300000000, 2)


main()