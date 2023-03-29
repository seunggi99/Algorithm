r,g,b = map(int,input().split())
count = 0
for i in range(0,r):
    for n in range(0,g):
        for m in range(0,b):
            print(i,n,m)
            count += 1

print(count)