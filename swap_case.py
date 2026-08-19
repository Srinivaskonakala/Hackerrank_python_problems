def swap_case(s):
    d=""
    for i in range(len(s)):
        if s[i]==s[i].lower():
            d+=s[i].upper()
        elif s[i]==s[i].upper():
            d+=s[i].lower()
    return d

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)