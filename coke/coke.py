def main():
    n = 50
    change(n)

def change(n):
    while n > 0:
        #prompt for amount due
        print(f'Amount Due: {n}')
        c = int(input('Insert Coin: '))
         #calcualte change
        if c == 25:
            n = n - 25
        if c == 10:
            n = n - 10
        if c == 5:
            n = n - 5
    owed = abs(n)
    #prompt again for the rest of amount
    print(f'Change Owed: {owed}')

main()