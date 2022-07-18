import sys

def main():


    ln=[]
    count=0


    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")


    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")


    try:



        ''' with open(filename,"r") as file:
            for line in file:
                    ln.append(line.strip())'''
        file = open(filename, 'r')
        lines = file.readlines()

        for line in lines:
            if not check_line(line):
                count += 1


    except FileNotFoundError:
        sys.exit("File does not exist")


    print(f'{count}')


def check_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False

if __name__ == "__main__":
    main()