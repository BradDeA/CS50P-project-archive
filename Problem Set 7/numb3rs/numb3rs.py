import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    count = 0
    if ':' in ip or ip.isalpha():
        return False
    if re.search(r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$', ip):
        list = ip.split('.')
        for i in list:
            if int(i) in range(0, 256):
                count += 1
        if count == 4:
            return True

    return False

if __name__ == "__main__":
    main()