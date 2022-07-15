# TODO: Complete os espaços em branco com uma solução possível
def main():
    name = input("What´s your name? ").strip()
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"


if __name__ == '__main__':
    main()


