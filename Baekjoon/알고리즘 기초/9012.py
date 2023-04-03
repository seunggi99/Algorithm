n = int(input())

for i in range(n):
    a = list(input())
    s = []
    k = 0   
    for n in range(len(a)):
        
        if a[0] == ")":
            print('NO')
            k = 1
            break
        elif a[n] == "(":
            s.append("(")
        elif a[n] == ")":
            if len(s) == 0:
                print('NO')
                k = 1
                break
            else:
                s.pop()
    if k == 0 and len(s) == 0:
        print("YES")
    elif k == 0 and len(s) != 0:
        print("NO")
