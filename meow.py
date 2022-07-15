def main():
    x = get_number()
    meow(x)

def get_number():
    while True:
        n = int(input("What´s number of meow! "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")


main()