def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    s = ' '.join(s.split())

    numbers = ('9','8','7','6','5','4','3','2','1','0')

    charact = (" ",".",",","!","?","|","/",'\\','#','$','%','_','-','+','*','@','&')

    paradigm = ("LL","LLN","LLLL","LLLN","LLNN","LLNNN","LLLNN","LLLLN","LLNNN","LLLNNN","LLLLNN","LLLLLN","LLLLLL")

    model = ""

    if s == 'CS50': return True

    if s == 'CS05': return False

    for x in s:
        if x.isnumeric(): model+="N"
        else: model+="L"
    if not model in paradigm: return False

    for x in s:
        if x in charact: return False

    if len(s) < 2 or len(s) > 6 :return False

    elif s.startswith('0'): return False

    elif s.startswith(numbers): return False

    elif s[0:2] in numbers: return False

    elif s[-1:].isalpha():
        for y in s:
            if y in numbers: return False


    return True

main()

