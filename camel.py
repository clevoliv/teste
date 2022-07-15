def main():
    name = input("Write some word in camelCase !")


    print("camelCase: ",(name))
    print("snake_case: ",convert(name))

def convert(s):
     #txt = ' '.join(txt.split())

     pos = [i for i, e in enumerate(s + 'A') if e.isupper()]
     parts = [s[pos[j]:pos[j + 1]] for j in range(len(pos) - 1)]

     if len(parts)>1:
         s = s[0:pos[0]] + '_' + str.casefold(parts[0]) + '_' + str.casefold(parts[1])

     elif len(parts)>0:
         s = s[0:pos[0]] + '_' + str.casefold(parts[0])
     else:
         return s

     return s

if __name__ == '__main__':
    main()