def main():
    f = input('Fraction: ')
    print(gauge(convert(f)))


def convert(fraction):
    try:
        s = fraction.split('/')
        x = int(s[0])
        y = int(s[1])
        p = round((x / y) * 100)
        if x > y:
            raise ValueError
    except (ValueError, ZeroDivisionError):
        raise

    #p = round((x / y) * 100)
    return p


def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return f'{percentage}%'



if __name__ == "__main__":
    main()