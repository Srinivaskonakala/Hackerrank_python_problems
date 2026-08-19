
from collections import namedtuple


n = int(input())

fields = input().split()

Point = namedtuple("Point", fields)

total = 0

for i in range(n):
    data = input().split()
    student = Point(*data)
    total += int(student.MARKS)

print(f"{total / n:.2f}")


