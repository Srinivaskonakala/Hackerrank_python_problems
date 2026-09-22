from itertools import product

k, m = map(int, input().split())

lists = []

for i in range(k):
    arr = list(map(int, input().split()))
    lists.append(arr[1:])

maximum = 0

for combination in product(*lists):
    value = sum(x ** 2 for x in combination) % m

    if value > maximum:
        maximum = value

print(maximum)