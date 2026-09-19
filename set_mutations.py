n=int(input())
a=set(map(int,input().split()))
m=int(input())
for i in range(m):
    b=input().split()
    if b[0]=="intersection_update":
        
        c=set(map(int,input().split()))
        a.intersection_update(c)
    elif b[0]=="update":
        c=set(map(int,input().split()))
        a.update(c)
    elif b[0]=="symmetric_difference_update":
        c=set(map(int,input().split()))
        a.symmetric_difference_update(c)
    elif b[0]=="difference_update":
        c=set(map(int,input().split()))
        a.difference_update(c)
print(sum(a))