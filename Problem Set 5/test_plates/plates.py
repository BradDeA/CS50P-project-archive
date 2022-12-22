def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isalpha() == False and s[1].isalpha() == False:
        return False
    if s[2] == '0':
        return False
    if len(s) == 6:
        if s[4].isalpha() == True and s[5].isdigit() == True:
            return False
    for c in s:
        if c in ['.', ' ', '!', '?', ',']:
            return False

    return True


if __name__ == "__main__":
    main()