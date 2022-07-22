import re

time = input("Hours: ").strip()

if re.search(r'(^([1-9]|0[1-9]|1[0-2])(\s)? ([AaPp][Mm])$)'
             r'|'
             r'(^([1-9]|0[1-9]|1[0-2]):[0-5][0-9] ([AaPp][Mm])$)', time, re.IGNORECASE):
    print("Valid")
else:

    print("Invalid")