import sys

def main():

    filename = sys.argv[2]
    ln=[]
    count=0


    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")


    try:

        with open(filename,"r") as file:
            for line in file:
                    ln.append(line.rstrip())


        for l in ln:
            if l == "" or l == "#":
                ...
            else:
                count=count+1


    except FileNotFoundError:
        sys.exit("File does not exist")


    print(f'{count}')


if __name__ == "__main__":
    main()