def main():
    out = date_convert()
    print(out)


def date_convert():
    #dict of month names & month number in order
    months = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12,
    }
    #prompt user for date fromatted in MM/DD/YYY or Month Day, Year, if not a valid date, prompt again
    while True:
        try:
            date = input('Date: ')

            #format date as YYYY-MM-DD & output
            if '/' in date:
                l = date.split('/')
                if l[0] in months:
                    pass
                #assume no more then 31 days
                elif int(l[1]) < 31 and int(l[0]) <= 12:
                    return f'{int(l[2]):02}-{int(l[0]):02}-{int(l[1]):02}'
                else:
                    pass
            else:
                l = date.split(' ')
                if l[0] in months and ',' in l[1]:
                    m = l[0]
                    d = l[1].replace(',', '')
                    if int(d) > 31:
                        pass
                    else:
                        return f'{int(l[2]):02}-{int(months[m]):02}-{int(d):02}'
        except ValueError:
            pass


main()
