def main():
    name = input("Write something to be trimmed !")
    print(trim(name))

def trim(txt):
     txt = ' '.join(txt.split()).replace(' ','...')
     return txt


if __name__ == '__main__':
    main()