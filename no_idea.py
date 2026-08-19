n,m=map(int,input().split())

arr1=list(map(int,input().split()))

A=set(map(int,input().split()))

B=set(map(int,input().split()))


happiness=0
for i in arr1:
    if i in A:
        happiness+=1
    elif i in B:
        happiness-=1
    else:
        happiness+=0
print(happiness)    

