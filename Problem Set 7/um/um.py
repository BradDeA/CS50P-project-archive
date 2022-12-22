import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r'\bum\b|\bUm\b', s)
    count = 0
    if match:
        for _ in match:
            count += 1
        return count

if __name__ == "__main__":
    main()