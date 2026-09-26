import numpy
arr=[]
n,m = map(int,input().split())
for i in range(n):
    row=list(map(int,input().split()))
    arr.append(row)
my_arr=numpy.array(arr)
result=numpy.min(my_arr,axis=1)

print(numpy.max(result))