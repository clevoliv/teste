def main():
    name = input("Write some greetings !")
    print(convert(name))

def convert(txt):
     txt = ' '.join(txt.split())
     if ':)' or ':(' in txt :
         txt = ' '.join(txt.split()).replace(':)',("\U0001F642"))

         txt = ' '.join(txt.split()).replace(':(', ("\U0001F641"))

     return txt

if __name__ == '__main__':
    main()