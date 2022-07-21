import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
        # preserving IP format
        if m:= re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip):
            # restricting the number range as valid
            if int(m[1])<256 and int(m[2])<256 and int(m[3])<256 and int(m[4])<256:
                return True

        return False


if __name__ == "__main__":
    main()