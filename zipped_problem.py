n,x=map(int,input().split())
arr=[]
for i in range(x):
    marks=list(map(float,input().split()))
    arr.append(tuple(marks))
for i in zip(*arr):
    print(sum(i)/x)
    

