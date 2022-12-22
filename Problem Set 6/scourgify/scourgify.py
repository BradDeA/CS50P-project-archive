import sys
import csv

def main():
    check_arg()

    try:
        csv_create(sys.argv[1])
    except:
        sys.exit('File does not exist')
#expects only 2 command line arguments
#read specified csv file
#split name,house columns into firstname,lastname,house
#write new information to new output csv file

def csv_create(argone):
    list = []
    with open(argone, 'r') as file:
        read = csv.DictReader(file)
        for row in read:
            last, first = row['name'].split(',')
            house = row['house']
            list.append({'first': first.lstrip(), 'last': last, 'house': house})

    csv_write(list)


def csv_write(list):
    with open(sys.argv[2], 'w') as csvtwo:
        write = csv.DictWriter(csvtwo, fieldnames=['first', 'last', 'house'])
        write.writeheader()
        write.writerows(list)


def check_arg():
    if len(sys.argv) > 3:
        sys.exit('Too many arguments')
    if len(sys.argv) < 3:
        sys.exit('Too few arguments')



if __name__ == '__main__':
    main()