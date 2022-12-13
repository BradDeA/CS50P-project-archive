def main():
    s = input('Input: ')
    print(shorten(s))


def shorten(word):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    newstr = ''

    for letter in range(len(word)):
        if word[letter] not in vowels:
            newstr = newstr + word[letter]

    return newstr


if __name__ == "__main__":
    main()