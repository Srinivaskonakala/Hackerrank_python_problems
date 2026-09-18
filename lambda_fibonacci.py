cube=lambda x: x**3
def fibonacci(n):
    res=[]
    a,b=0,1
    for i in range(n):
        res.append(a)
        a,b=b,a+b
    return res

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))