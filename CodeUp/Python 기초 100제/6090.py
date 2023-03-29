a, m, d, n = map(int,input().split())
count = 1
while 1:
    if count == n:
        print(a)
        break
    a = a*m+d
    count += 1