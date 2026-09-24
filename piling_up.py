t = int(input())

for _ in range(t):
    n = int(input())
    blocks = list(map(int, input().split()))

    left = 0
    right = n - 1
    previous = float('inf')

    possible = True

    while left <= right:

        if blocks[left] >= blocks[right]:
            current = blocks[left]
        else:
            current = blocks[right]

        if current > previous:
            possible = False
            break

        previous = current

        if blocks[left] >= blocks[right]:
            left += 1
        else:
            right -= 1

    if possible:
        print("Yes")
    else:
        print("No")