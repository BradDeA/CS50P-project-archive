import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.search(r'([0-9]*)(:?)([0-9]*) (AM|PM) to ([0-9]*)(:?)([0-9]*) (AM|PM)', s)
    if match:
        groups = match.groups()
        if int(groups[0]) > 12 or int(groups[4]) > 12:
            raise ValueError
        if groups[3] == groups[7]:
            raise ValueError

        firstform = format(groups[0], groups[2], groups[3])
        secondform = format(groups[4], groups[6], groups[7])
        return f'{firstform} to {secondform}'
    else:
        raise ValueError

def format(hr, mn, ampm):
    if ampm == 'AM' and int(hr) == 12:
        return '00:00'

    elif ampm == 'AM' and mn != '':
        if int(mn) > 59:
            raise ValueError
        return f'{int(hr):02}:{mn}'

    elif ampm == 'AM' and mn == '':
        return f'{int(hr):02}:00'

    if ampm == 'PM' and int(hr) == 12:
        return '12:00'

    elif ampm == 'PM' and mn != '':
        if int(mn) > 59:
            raise ValueError
        if int(hr) < 12:
            return f'{int(hr) + 12:02}:{mn}'
        elif int(hr) == 12:
            return f'{int(hr)}:{mn}'

    elif ampm == 'PM' and mn == '':
        if int(hr) < 12:
            return f'{int(hr) + 12:02}:00'
        else:
            return f'{int(hr):02}:00'

if __name__ == "__main__":
    main()