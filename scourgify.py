import sys
import csv

def main():



    table = []
    count=0


    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")


    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a Python file")


    try:

        with open(filename) as file:
            #fieldnames = ['name', 'house']
            reader = csv.DictReader(file)

            for row in reader:
                table.append({"first": row['name'].split(",")[1].lstrip(),"last": row['name'].split(",")[0], "house": row["house"]})



    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], 'w') as f:

        writer = csv.DictWriter(f, fieldnames=["first","last","house"])
        #writer.writerow({"first":"first", "last": "last", "house":"house"})
        writer.writeheader()

        for row in table:
            writer.writerow({"first":row["first"], "last": row["last"], "house":row["house"]})

        #print(f"{x['firstname']} {x['lastname']}, {x['house']}")




if __name__ == "__main__":
    main()