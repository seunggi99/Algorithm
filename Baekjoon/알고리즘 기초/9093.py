a = int(input())

c = []

for i in range(a):
    b = input().split()
    c.append(b)

for i in range(a):
    for n in range(len(c[i])):
        print(c[i][n][::-1], end=" ")
    print()