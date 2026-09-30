t=int(input())
for i in range(t):
    string=input()
    try:
        float(string)
        if "." in string:
            print("True")
        else:
            print("False")
    except:
        print("False")