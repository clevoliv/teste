import emoji

def main():
    name = input("Input something to emojize !")

    print(emoji.emojize(str.lower(name)))

main()

