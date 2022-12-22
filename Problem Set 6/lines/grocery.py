def main():
    g = grocery_list()
    print(g)


def grocery_list():
    #empty dict
    list = {}
    while True:
        try:
            #prompt for input one at a time & translate string to uppercase
            item = input().upper()
            #save items & quantity to dict
            if item not in list:
                list[item] = 0
            #if item already in dict, add 1 to quantity
            if item in list:
                list[item] += 1
            #control-d to cancel & ouput dict
        except EOFError:
            #print alphabetically
            for item, quantity in sorted(list.items()):
                print(f'{quantity} {item}')
            return ''



main()
