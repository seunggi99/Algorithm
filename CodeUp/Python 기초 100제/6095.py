a = int(input())
n = 19
m = 19
list = [[0]*m for _ in range(n)]
for i in range(a):
    x, y = map(int,input().split())
    list[x-1][y-1] = 1

for i in range(19):
    for k in range(19):
        print(list[i][k],end=" ")
    print('')