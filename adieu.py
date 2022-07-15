def main():


    mount()


def get_list():
    item = []

    while True:



        try:
            key=input("Name: ").title()
            item.append(key)

            '''if key =='1': return item'''


        except KeyboardInterrupt:
            return item
        except EOFError:
            return item

def mount():

    itens = get_list()

    mnt = list(itens)

    item = int()

    if len(mnt) == 1:
        print(f' Adieu, adieu, to {mnt[0]}')

    if len(mnt) == 2:
        print(f' Adieu, adieu, to {mnt[0]} and {mnt[1]}')

    if len(mnt) >= 3:
        mid = ' '.join((mnt[1:-1])).replace(' ', ', ')

        print(f' Adieu, adieu, to {mnt[0]}, {mid}, and {mnt[-1]}')




if __name__ == '__main__':
    main()