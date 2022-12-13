import inflect

inf = inflect.engine()

def main():
    a = adieu()
    print(a)

def adieu():
    namelist = []
    while True:
        try:
            names = input('Name: ')
            namelist.append(names)
        except EOFError:
            bid_adieu = inf.join((namelist))
            return f'\nAdieu, adieu, to {bid_adieu}'


main()