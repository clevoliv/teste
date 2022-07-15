import random

def main():
    lv = input("Level:")
    lv = int(get_int_number(lv))

    guess = random.randint(1,lv)

    get_int_number1(guess,lv)




def get_int_number(n):
    while True:

        try:

            if int(n)> 0: return n

            n = (input("Level: "))


        except ValueError:
            n = (input("Level: "))
            pass

def get_int_number1(guess,lv):
    while True:

        try:
            n = int(input("Guess: "))

            if int(n)> 0 and int(n)<=int(lv):

                if n < guess:
                    print("Too small!")

                elif n > lv or n > guess:
                    print("Too large!")

                else:
                    print('Just right!')
                    return n

            n = (input("Guess: "))


        except ValueError:
            n = (input("Guess: "))
            pass

if __name__ == '__main__':
    main()