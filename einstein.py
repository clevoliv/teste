# TODO: Complete os espaços em branco com uma solução possível
def main():
    x = get_int_number()

    print(f"m: {x}")
    print(f"E: {mass_energy(x)}")

def mass_energy(n):
    return n * pow(300000000 , 2)

def get_int_number():
    while True:

        try:
            n = int(input("Input the body mass in (kg) "))
            if n >= 0: return n
            print("Number has to be bigger than zero!")
        except ValueError:
            pass


if __name__ == '__main__':
    main()
