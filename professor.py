import random


def main():
        n = get_level()
        err = 0

        for _ in range(10):
            x= generate_integer(n)
            y = generate_integer(n)
            err = get_answer(x,y, err)

        print(f'Score of: {10 - err}')



def get_level():
        while True:

            try:

                n = int(input("Level: "))

                if 0 < int(n) < 4: return n

            except ValueError:
                n = (input("Level: "))


def generate_integer(level):
        while True:

            try:

                if level == 1:


                        problem = (random.randint(0, 9))
                        return problem



                elif level == 2:


                        problem = (random.randint(10, 99))
                        return problem



                else:


                        problem = (random.randint(100, 999))
                        return problem



            except ValueError:
                pass


def get_answer(x,y, ir):
        item = []

        total = 0


        while True:

            try:

                print(f'{x} + {y} =')
                key = int(input(""))


                if key == (x+y):
                    item.append(key)

                    return ir
                else:
                    total = total + 1
                    if total < 3:
                        print("EEE")

                        if total < 2: ir = ir + 1

                    else:
                        print(f'{x} + {y} = {x+y}')

                        return ir


            except ValueError:
                total = total + 1
                if total < 3:
                    print("EEE")

                    if total < 2: ir = ir + 1

                else:
                    print(f'{x} + {y} = {x+y}')

                    return ir
            except EOFError:
                pass


if __name__ == "__main__":
        main()