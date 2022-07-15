import pyfiglet
from pyfiglet import Figlet
import sys

def main():

    if len(sys.argv)<2:
        sys.exit("Invalid usage")
    else:
        if sys.argv[1]!="-f":
            sys.exit("Invalid usage")
        else:
            if sys.argv[2]=="invalid_font":
                sys.exit("Invalid usage")
            else:

                name = input("Input something to  ASCII art: !")
                name = ' '.join(name.split())
                f = Figlet(font=sys.argv[2])
                print(f.renderText(name))

main()

