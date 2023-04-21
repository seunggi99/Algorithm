N = int(input())
d = [0,1]

for i in range(2, N+1):
    m = 1e9
    j = 1

    while (j**2) <= i:
        m = min(m, d[i - (j**2)])
        j += 1

    d.append(m + 1)
print(d[N])