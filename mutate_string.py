def mutate_string(string, position, character):
    lst=[]
    for i in range(len(string)):
        lst.append(string[i])
    for i in range(1,len(lst)):
        if i==int(position):
            lst[i]=character

            
    return "".join(lst)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)