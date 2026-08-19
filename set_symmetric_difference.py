a=int(input())
arr1=set(map(int,input().split()))
b=int(input())
arr2=set(map(int,input().split()))
symmetric_difference=arr1.symmetric_difference(arr2)
for i in sorted(symmetric_difference):
    print(i)