import re
import sys


def main():
    #get time from user and capitalize
    print(convert(input("Hours: ")).strip())


def convert(s):

    try:

        if validate_format(s):
            m = re.search(r"to", s)
            srt = (s[:m.start()]).strip()
            end = (s[m.end():]).strip()

            if srt[-2:] == "AM":

                txt = ' '.join(srt.split()).replace('AM', '')

                if ':' in txt:
                    z = txt.rsplit(':')
                else:
                    z = txt.rsplit()
                    z.append(0)

                txt = int(z[0]) + int(z[1]) / 60

                txt1 = ' '.join(end.split()).replace('PM', '')

                if ':' in txt1:
                    z1 = txt1.rsplit(':')
                else:
                    z1 = txt1.rsplit()
                    z1.append(0)

                x = int(z1[0]) + 12

            else:
                txt1 = ' '.join(srt.split()).replace('PM', '')

                if ':' in txt1:
                    z1 = txt1.rsplit(':')
                else:
                    z1 = txt1.rsplit()
                    z1.append(0)

                x = int(z1[0]) + 12

                txt = ' '.join(end.split()).replace('AM', '')

                if ':' in txt:
                    z = txt.rsplit(':')
                else:
                    z = txt.rsplit()
                    z.append(0)

                txt = int(z[0]) + int(z[1]) / 60


                return (f"{int(x):02}:{int(z1[1]):02} to {int(z[0]):02}:{int(z[1]):02}").lower()

            return (f"{int(z[0]):02}:{int(z[1]):02} to {int(x):02}:{int(z1[1]):02}").lower()



        else:
            raise ValueError()

    except (ValueError):
    # informed string does not match the expected format
        raise




def validate_format(s):

    try:
        # recognizing str format
        if m := re.search(r"to", s):
            srt = (s[:m.start()]).strip()
            end = (s[m.end():]).strip()


            #validating hours/period format
            if (srt:= re.search(r'^([1-9]|0[1-9]|1[0-2])(\s)? ([AaPp][Mm])$|(^([1-9]|0[1-9]|1[0-2]):[0-5][0-9] ([AaPp][Mm])$)', srt)) \
                    and \
                (end:= re.search(r'^([1-9]|0[1-9]|1[0-2])(\s)? ([AaPp][Mm])$|(^([1-9]|0[1-9]|1[0-2]):[0-5][0-9] ([AaPp][Mm])$)', end)):
                return True

        else:
            raise ValueError()


    except (ValueError):
    # informed string does not match the expected format
        raise



if __name__ == "__main__":
    main()