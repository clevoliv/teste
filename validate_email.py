import re

email = input("Type your email ").strip()

if re.search("^\w+@(\w+\.)?\w+\.(com|edu|gov|org|net)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")