def main():
    name = input("Please provide fle name com it extension !")

    print(discover(str.lower(name)))


def discover(txt):
    txt = ' '.join(txt.split())

    if txt.endswith(".gif"):
        txt = 'image/gif'

    elif txt.endswith(".jpg") or txt.endswith(".jpeg"):
        txt = 'image/jpeg'

    elif txt.endswith(".png"):
        txt = 'image/png'

    elif txt.endswith(".pdf"):
        txt = 'application/pdf'

    elif txt.endswith(".txt"):
        txt = 'text/plain'

    elif txt.endswith(".zip"):
        txt = 'application/zip'

    else:
        txt = 'application/octet-stream'

    return txt

main()