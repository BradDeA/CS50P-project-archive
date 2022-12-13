def main():
    o = order()
    print(o)


def order():
    menuitems = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    t = 0

    while True:
        try:
            #prompt for menu item
            item = input('Item: ').title()
            #ignore non menu items items
            if item in menuitems:
                t += menuitems[item]
                #display total cost after every item
                print(f'${t}0')


#EOFError to end with control-d input
        except EOFError:
            return ''

main()
