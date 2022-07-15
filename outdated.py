import datetime

def main():

    dt = format_dt()

    y = int(dt[2])
    m = int(dt[0])
    d = int(dt[1])

    x = datetime.datetime(int(y), int(m), int(d))
    print(x.strftime("%Y") + '-' + x.strftime("%m") + '-' + x.strftime("%d"))


def format_dt():
    while True:

        try:
            dt0 = input("Inform a date in format month-day-year! ").title()

            '''dt = ' '.join(dt.split())'''

            if '-' in dt0 or ',' in dt0 or '/' in dt0:
                dt = ' '.join(dt0.split()).replace('/', '-').replace(', ', '-').replace(' ', '-')
                dt = dt.split('-')

                if dt[0].isalpha() and ('/' not in dt0) and (int(dt[1]) < 31 or dt[1] < '31'):


                    m = datetime.datetime.strptime(dt[0], "%B").month
                    dt[0] = m
                    return dt

                elif (dt[0]<'13' or int(dt[0])<13) and (dt[1].isnumeric()) and (int(dt[1])<32):
                    m = int(dt[0])
                    return dt

                else :
                    print("Wrong format")

            else:
                print("Wrong format")



        except ValueError:
            pass

if __name__ == "__main__":
    main()