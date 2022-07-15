def main():
    fr = input("Inform a fraction, formatted as X/Y! ")

    percentage = convert(fr)

    z = gauge(percentage)

    print(z)


def convert(fraction):
    while True:

        try:
            n = ''.join(fraction).replace('"', '').replace("'", "").replace(' ', '')
            n = n.split('/')

            if n[0].isnumeric() and n[1].isnumeric():
                x = int(n[0])
                y = int(n[1])
            else:
                raise ValueError()

            if y == 0:
                raise ZeroDivisionError()
            if int(x) > int(y):
                raise ValueError()

            if int(x) <= int(y):
                return round((int(x) / int(y)) * 100)



        except  ZeroDivisionError:
            # n = (input("Inform a denominator different from zero! "))
            raise
        except  IndexError:
            fraction = (input("Inform a fraction, formatted as numbers X/Y! "))
            pass
        except ValueError:
            # n = (input("Inform a fraction, formatted as numbers X/Y! "))
            raise


def gauge(percentage):
    if percentage <= 1:
        return ("E")

    elif percentage >= 99:
        return ("F")

    else:
        return (f'{percentage:.0f}%')


if __name__ == "__main__":
    main()