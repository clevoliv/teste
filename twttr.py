def main():
    name = input("Write something to Tweet !")

    print("snake_case: ", shorten(name))

def shorten(word):

    newstr = word

    if str.upper(word)=='CS50':
        newstr=str.upper(word)
        return newstr
    else:


        vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
        for x in word:
            if x in vowels:
                newstr = newstr.replace(x,"")

    return newstr

if __name__ == '__main__':
    main()