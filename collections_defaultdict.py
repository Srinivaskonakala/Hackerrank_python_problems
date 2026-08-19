n,m=map(int,input().split())
lst1=[]
for i in range(n):
    A=input()
    lst1.append(A)
lst2=[]
for i in range(m):
    B=input()
    lst2.append(B)

for i in lst2:
    positions=[]
    for j in range(n):
        if i==lst1[j]:
            positions.append(j+1)
    if positions:
        print(*positions)
    else:
        print(-1)