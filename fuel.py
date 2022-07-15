def main():
    fr = input("Inform a fraction, formatted as X/Y! ")

    z = get_int_number(fr)

    z = int(z[0]) / int(z[1])

    if z<=0.01:
            print("E")

    elif z>=0.99:
            print("F")

    else:
            print(f'{z * 100:.0f}%')

def get_int_number(n):
    while True:

        try:
            n = n.split('/')
            x = int(n[0])
            y = int(n[1])


            if int(x) > int(y):
                n = (input("Inform a denominator higher than numerator! "))
            if int(y)==0:
                n = (input("Inform a denominator different from zero! "))

            if int(x) <= int(y): return n


        except ValueError:
            n = (input("Inform a fraction, formatted as numbers X/Y! "))
            pass
        except  ZeroDivisionError:
            n = (input("Inform a denominator different from zero! "))
            pass
        except  IndexError:
            n = (input("Inform a fraction, formatted as numbers X/Y! "))
            pass

main()