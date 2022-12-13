def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(percent)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    s = d.strip('$')
    a = float(s)
    return a


def percent_to_float(p):
    n = p.strip('%')
    i = '0.' + n
    c = float(i)
    return c


main()