a=set(map(int,input().split()))
n=int(input())
result=True
for i in range(n):
    set_n=set(map(int,input().split()))
    if not a.issuperset(set_n):
        result=False
    
print(result)
