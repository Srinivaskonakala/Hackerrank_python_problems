from collections import Counter
size=int(input())
room_numbers=list(map(int,input().split()))

counter=Counter(room_numbers)
for char,number in counter.items():
    if number==1:
        print(char)