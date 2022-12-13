def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Must contain a max of 6 and a min of 2 characters
        # Check length of string, if between 2 & 6, continue
    if len(s) < 2 or len(s) > 6:
        return False

    # Must start with 2 letters
        # Check if the first 2 characters in the string are letters
    if s[0].isalpha() == False and s[1].isalpha() == False:
        return False

    # Numbers must come at the end of the string, check the first number is not 0
    if s[2] == '0':
        return False

    # Check for letters within the string
    if len(s) == 6:
        if s[4].isalpha() == True and s[5].isdigit() == True:
            return False

    # No periods, spaces or punctuation
        # Check for periods, spaces, punctuation
    for c in s:
        if c in ['.', ' ', '!', '?', ',']:
            return False

    return True

main()