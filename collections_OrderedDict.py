from collections import OrderedDict
n=int(input())
d=OrderedDict()
for i in range(n):
    item, price=input().rsplit(" ",1)
    price=int(price)
    if item in d:
        d[item]+=price
    else:
        d[item]=price
for item,price in d.items():
    print(item,price)
