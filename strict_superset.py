a=set(map(int,input().split()))
n=int(input())
for i in range(n):
    set_n=set(map(int,input().split()))
print(a.issuperset(set_n))