from tabulate import tabulate
import sys

def main():
#checks for exactly 1 command line argument
    argcheck()

    try:
        pizza(sys.argv[1])
    except:
        sys.exit('File not found')

def pizza(arg):
    menu = []
#open .csv file
    with open(arg) as file:
#create table with information inside .csv file
        for line in file:
            item = line.strip().split(',')
            menu.append(item)
#output table with tabulate using grid format
        print(tabulate(menu, headers='firstrow', tablefmt='grid'))

def argcheck():
    if len(sys.argv) < 2:
        sys.exit('Too few arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many arguments')
    if '.csv' not in sys.argv[1]:
        sys.exit('Not a CSV file')


if __name__ == '__main__':
    main()