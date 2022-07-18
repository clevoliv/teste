import sys
import csv
from tabulate import tabulate


def main():



    table = []
    count=0


    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")


    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a Python file")


    try:

        with open(filename) as file:
            fieldnames = ['Regular Pizza', 'Small','Large']
            reader = csv.DictReader(file,fieldnames=fieldnames)

            for row in reader:
                table.append({"Regular Pizza": row["Regular Pizza"], "Small": row["Small"],"Large": row["Large"]})



    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(table, tablefmt="grid", headers="firstrow"))





if __name__ == "__main__":
    main()