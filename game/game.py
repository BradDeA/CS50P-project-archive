import random
import sys

def main():
    generator()

def generator():
    while True:
        try:
            l = int(input('Level: '))
        except ValueError:
            generator()
        if l > 0:
            guesser(l)


def guesser(i):
    num = random.randint(1, i)
    while True:
        try:
            g = int(input('Guess: '))
            if g > num:
                print('Too large!')
            elif g < num:
                print('Too small!')
            elif g == num:
                sys.exit('Just right!')
        except ValueError:
            pass


main()