def main():
    fr = input("Inform a fraction, formatted as X/Y! ")

    percentage = convert(fr)

    z = gauge(percentage)

    print(z)


def convert(fraction):
    while True:
        index = fraction.find("/")

        try:
            x = int(fraction[:index])
            y = int(fraction[index+1:])

            if int(x) > int(y):
                fraction = input("Inform a fraction, formatted as X/Y! ")
                continue
            else:
                return round((int(x) / int(y)) * 100)

        except (ValueError, ZeroDivisionError):
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