def main():
    time = input("What time is it ?")

    print(f"{meal_time(str.lower(time))}")


def meal_time(n):

    n=float(converter(n))

    if 7.0<=n<=8.0:
            return ("breakfast time")

    elif 12.0<=n<=13.0:
            return ("lunch time")

    elif 18.0<=n<=19.0:
            return ("dinner time")

    else:
            return

def converter(s):

    if ":" not in s :
        n= format_time()

        return converter(n)

    else:


       if s[-2:] == "am" or s[-4:] == "a.m." :
           txt = ' '.join(s.split()).replace('am', '').replace('a.m.', '')

           z = txt.rsplit(':')

           txt = int(z[0]) + int(z[1]) / 60
       else:
          if s[-2:] == "pm" or s[-4:] == "p.m.":
              txt = ' '.join(s.split()).replace('pm', '').replace('p.m.', '')
              z = txt.rsplit(':')
              x = int(z[0]) + 12

              txt = x + int(z[1]) / 60
          else:
              z = s.rsplit(':')

              txt = int(z[0]) + int(z[1]) / 60
    return txt


def format_time():
    while True:

        try:
            t = (input("Input time containing ':' ! "))
            if ":" in t : return t
            print("Time has to have separator with ':' !")
        except ValueError:
            pass

if __name__ == "__main__":
    main()