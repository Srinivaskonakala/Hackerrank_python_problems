import re

T = int(input())

for _ in range(T):
    S = input()
    try:
        re.compile(S)
        if '++' in S or '**' in S or '*+' in S or '+*' in S or '??' in S:
            print(False)
        else:
            print(True)
    except re.error:
        print(False)