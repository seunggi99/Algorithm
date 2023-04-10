n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = []
a.sort(reverse = True)
for i in range(n):
    if len(c) == 0:
        c.append(i)
    else:
        for m in range(len(c)):
            if b[i] <= b[c[m]]:
                c.insert(m,i)
                break
            elif m == len(c)-1:
                c.append(i)

newa = [[0] for _ in range(n)]
for i in range(n):
    newa[c[i]] = a[i]

s = 0

for i in range(n):
    s += newa[i]*b[i]
print(s)