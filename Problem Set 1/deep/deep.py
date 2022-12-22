def main():
    a = input('What is the answer to the Great Question of Life, the Universe and Everything?\n')
    n = a.casefold().strip()
    print(check(n))

def check(to):
    if to == '42':
        return 'Yes'
    if to == 'forty-two':
        return 'Yes'
    if to == 'forty two':
        return 'Yes'
    else:
        return 'No'

main()