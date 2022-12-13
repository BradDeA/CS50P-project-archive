from datetime import date
import sys
import re
import inflect

p = inflect.engine()

def main():
    born_on = input('Date of Birth: ')
    if format_check(born_on) == True:
        text = born_on.split('-')
        print(minutes(text))

def minutes(list):
    minutes = (date.today() - date(int(list[0]), int(list[1]), int(list[2]))).days * 24 * 60
    text = p.number_to_words(minutes, andword='')
    return f'{text.capitalize()} minutes'

def format_check(d):
    d = re.search(r'([0-9][0-9][0-9][0-9])-([0-9][0-9])-([0-9][0-9])', d)
    if d:
        return True
    else:
        sys.exit('Invalid date')

if __name__ == "__main__":
    main()