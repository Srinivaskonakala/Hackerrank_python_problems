import re

n = int(input())

for i in range(n):

    card = input()

    # Check the format
    if re.fullmatch(r'[4-6]\d{15}', card):
        number = card

    elif re.fullmatch(r'[4-6]\d{3}(-\d{4}){3}', card):
        number = card.replace("-", "")

    else:
        print("Invalid")
        continue

    # Check for 4 consecutive same digits
    if re.search(r'(\d)\1\1\1', number):
        print("Invalid")
    else:
        print("Valid")