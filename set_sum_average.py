def average(array):
    arrs=set(array)
    return sum(arrs)/len(arrs)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)