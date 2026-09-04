n = int(input())

words = {}

for _ in range(n):
    word = input().strip()
    words[word] = words.get(word, 0) + 1

print(len(words))
print(*words.values())