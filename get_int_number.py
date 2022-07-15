def main():
    x = get_int_number()
    print(f"The number is {x} !")

def get_int_number():
    while True:

        try:
            n = int(input("What´s the number! "))
            return n
        except ValueError:
            pass

main()