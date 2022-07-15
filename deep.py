def main():
    name = input("What is your answer to the Great Question of Life, the Universe and Everything ?")

    print(convert(str.lower(name)))


def convert(txt):
    txt = ' '.join(txt.split())
    if txt =='forty two' or txt =='forty-two' or txt == '42':
        txt = 'Yes'

    else:

        txt = 'No'

    return txt

main()
