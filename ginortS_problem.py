
s=input()
lower=[]
upper=[]
odd=[]
even=[]
for i in s:
    if i.islower():
        lower.append(i)
        lower.sort()
    elif i.isupper():
        upper.append(i)
        upper.sort()
    elif int(i)%2==1:
        odd.append(i)
    else:
        even.append(i)       
print("".join(lower+upper+odd+even))