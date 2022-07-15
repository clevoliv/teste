def main():


    organize()


def get_list():
    item = []

    while True:



        try:
            key=input("Add your itens !").upper()
            item.append(key)

            '''if key.isalpha():'''

            '''else: return item'''



        except KeyboardInterrupt:
            return item
        except EOFError:
            return item

def organize():
    itens = get_list()

    org = list(set(itens))

    org.sort()


    for item in range(len(org)):
        count = itens.count(itens[item])
        print(f'{count} {org[item]}')


if __name__ == '__main__':
    main()