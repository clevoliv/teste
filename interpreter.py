def main():
    name = input("Please provide the arithmetic expression !")

    print(f"{converter((name)):.1f}",)


def converter(txt):
    txt = ' '.join(txt.split())


    if "+" in txt:
        z = txt.rsplit('+')

        txt = int(z[0])+int(z[1])

    elif "-" in txt:
        z = txt.rsplit('-')
        txt = int(z[0])-int(z[1])

    elif "*" in txt:
        z = txt.rsplit('*')
        txt = int(z[0])*int(z[1])

    else:
        z = txt.rsplit('/')

        if int(z[1])==0:
            txt = int(z[0])/non_zero_number()

        else:

            txt = int(z[0])/int(z[1])

    return txt

def non_zero_number():
        while True:

            try:
                n = int(input("Input non_zeo number! "))
                if n > 0: return n
                print("Number has to be bigger than zero!")
            except ValueError:
                pass



main()