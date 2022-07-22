import re
import sys


def main():
    print(count(input("Text: ").lower()))


def count(s):

    m = re.findall(r"(\bum\W)|(\sum\b)|(\bUm\W)|(\sUm\b)|(\bUM\W)|(\sUM\b)|(\bum\b)|(\bUm\b)|(\bUM\b)", s)

    z = len(m)

    return int(z)


if __name__ == "__main__":
    main()