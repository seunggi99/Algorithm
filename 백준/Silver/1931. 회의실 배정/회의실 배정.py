n = int(input())
lst=[]
for i in range(n):
    l = list(map(int,input().split()))
    lst.append(l)

lst.sort(key=lambda x: (x[1], x[0]))

x = 0
while x <= n-2:
    if lst[x+1][0] < lst[x][1]:
        del[lst[x+1]]
        n -= 1
    else:
        x += 1

print(n)