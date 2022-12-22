from pyfiglet import Figlet
import random
import sys

figlet = Figlet()


def main():
    if len(sys.argv) == 3:
        font = font_to_text()
        print(font)
    elif len(sys.argv) == 1:
        font = random_font()
        print(font)
    else:
        sys.exit('Invalid Usage')


def font_to_text():
    if sys.argv[1] in ['-f', '-font'] and sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=f'{sys.argv[2]}')
        t = input('Input: ')
        return figlet.renderText(t)
    else:
        sys.exit('Invalid Usage')


def random_font():
    s = random.choice(figlet.getFonts())
    figlet.setFont(font=f'{s}')
    t = input('Input: ')
    return figlet.renderText(t)


main()