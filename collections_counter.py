# from collections import Counter
# lst=list(map(int,input().split()))
# print(Counter(lst))
# print(Counter(lst).items())
# print(Counter(lst).keys())
# print(Counter(lst).values())
n=int(input())
lst=list(map(int,input().split()))
a=int(input())
total=0
for i in range(a):
    size,price=map(int,input().split())
    
    if size in lst:
        lst.remove(size)
        total+=price
print(total)