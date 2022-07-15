def main():
    n=0
    change(n)

def change(n):
    while True:

        x=50
        coins = ["5","10","25","50"]

        try:
            c = int(input("Insert a cent coin! "))

            if c == 50:
                print("Changed Owed: ", x-c)
                return (x-n)

            elif c == 25:
                n = n + c

                if x > n:
                    print("Amount Due: ", x - n)

                else:
                    print("Changed Owed: ", abs(x - n))
                    return (x - n)

            elif c == 10:
                n = n + c
                if x > n:
                    print("Amount Due: ", x - n)

                else:
                    print("Changed Owed: ", abs(x - n))
                    return (x - n)

            elif c == 5:
                n = n + c
                if x > n:
                    print("Amount Due: ", x - n)

                else:
                    print("Changed Owed: ", abs(x - n))
                    return (x - n)

            else:
                print("Amount Due: ", x)

        except ValueError:
            pass

    return n

if __name__ == '__main__':
    main()


