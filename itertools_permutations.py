from itertools import permutations
s,k=input().split(" ")
k=int(k)

for i in range(len(list(permutations(s,k)))):
    print("".join(list(permutations(s,k))[i]))
    lexico = sorted(list(permutations(s,k)))
    print("".join(lexico[i]))