def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    x = get_order(menu,'key')



def get_order(menu,key):
    item = []
    total = 0
    while True:



        try:
            key=input("Add your itens !").title()

            if key in menu:
                    item.append(key)
                    total = total + float(menu[item[-1]])

                    print(f"Total: ${total:.2f}")



        except KeyboardInterrupt:
            return item
        except EOFError:
            return item

if __name__ == '__main__':
    main()