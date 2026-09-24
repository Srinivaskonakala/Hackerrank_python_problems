t=int(input())
for i in range(t):
    uid=input()
    if len(uid)!=10:
        print("Invalid")
        continue
    if not uid.isalnum():
        print("Invalid")
        continue
    if len(set(uid))!=10:
        print("Invalid")
        continue
    uppercase=0
    digits=0
    for char in uid:
        if char.isupper():
            uppercase+=1
        elif char.isdigit():
            digits+=1
    if uppercase<2 or digits<3:
        print("Invalid")
    else:
        print("Valid")