def main():
    time = input('Time: ')
    print(convert(time))

def convert(time):
    h, m = time.split(':')
    m = float(m) / 60
    n = float(h) + m

    if n > 6.9 and n < 8.01:
        return 'Breakfast Time'
    if n > 11.9 and n < 13.01:
        return 'Lunch Time'
    if n > 17.9 and n < 19.01:
        return 'Dinner Time'

if __name__ == '__main__':
    main()