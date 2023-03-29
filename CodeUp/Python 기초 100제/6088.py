a, d, n = map(int,input().split())
count = 1
while 1:
    if count == n:
        print(a)
        break
    a += d
    count += 1