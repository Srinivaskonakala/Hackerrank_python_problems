from itertools import combinations
n=int(input())
s=input().split()
k=int(input())
count=0
total=0
for i in combinations(s,k):
    total+=1
    if "a" in i:
        count+=1
print(f"{count/total:.3f}")

