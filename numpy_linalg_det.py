import numpy

a=int(input())
arr=[]
for i in range(a):
    row=list(map(float,input().split()))
    arr.append(row)
arr=numpy.array(arr)

print(numpy.linalg.det(arr))