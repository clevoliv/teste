import re

name = input("What´s your name? ")
new_quote = re.sub(r"\s{2}", "", name)
new_quote = ' '.join(new_quote.split()).replace(' ','...')

print(new_quote)