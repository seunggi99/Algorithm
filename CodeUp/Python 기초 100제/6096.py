n = 19
m = 19
dlist = [[0]*m for _ in range(n)]

for i in range(19):
    a = list(input().split())
    for n in range(19):
        dlist[i][n] = int(a[n])

a = int(input())
for i in range(a):
    x, y = map(int,input().split())

    for n in range(19):
        if dlist[n][y-1] == 1 : 
            dlist[n][y-1] = 0
        else:
            dlist[n][y-1] = 1

    for m in range(19):
        if dlist[x-1][m] == 1 : 
            dlist[x-1][m] = 0
        else:
            dlist[x-1][m] = 1

for i in range(19):
    for k in range(19):
        print(dlist[i][k],end=" ")
    print()