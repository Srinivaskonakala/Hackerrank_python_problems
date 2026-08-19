# Errors detected during execution are called exceptions.
n=int(input())
for i in range(n):
    try:
        a,b=map(int,input().split())
        print(a//b)
        
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)

