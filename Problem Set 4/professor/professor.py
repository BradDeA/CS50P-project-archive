import random


def main():
    score = 0
    round_num = 0

    level = get_level()
    while round_num < 10:
        first, second = generate_integer(level)
        if round(first, second) == True:
            score += 1
        round_num += 1

    print(score)

def get_level():
    while True:
        try:
            l = int(input('Level: '))
            if l in [1, 2, 3]:
                return l
        except:
            pass

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

def round(x, y):
    count = 1
    while count <= 3:
        try:
            a = int(input(f'{x} + {y} = '))
            if a == (x + y):
                return True
            else:
                print('EEE')
                count += 1
        except:
            print('EEE')
            count += 1
    print(f'{x} + {y} = ', x + y)

if __name__ == "__main__":
    main()