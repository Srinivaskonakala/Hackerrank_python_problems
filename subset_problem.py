t=int(input())
for i in range(t):
    len_a=int(input())
    a=set(map(int,input().split()))
    len_b=int(input())
    b=set(map(int,input().split()))
    print(a.issubset(b))