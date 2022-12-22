def main():
    s = input('Input: ')
    remove_vowels(s)

def remove_vowels(str):
    #list of vowels
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    newstr = ''

    #search string for vowels
    for letter in range(len(str)):
        if str[letter] not in vowels:
            newstr = newstr + str[letter]

    #print new string
    print(newstr)


main()