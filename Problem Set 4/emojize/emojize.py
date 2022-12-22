import emoji

def main():
    e = emoji_maker()
    print(e)


def emoji_maker():
#prompt user for string
    moji = input('Input:  ')
#convert string to emoji convert both sring or alias
    return emoji.emojize(moji, language='alias')

main()