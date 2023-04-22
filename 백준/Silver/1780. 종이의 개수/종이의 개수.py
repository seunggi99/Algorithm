n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

one = 0
zero = 0
mone = 0


def d(x, y, n):
    global one, zero, mone

    check = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != graph[i][j]:
                check = -2
                break

    if check == -2:
        n = n // 3
        d(x, y, n)
        d(x, y + n, n)
        d(x, y + 2 * n, n)
        d(x + n, y, n)
        d(x + n, y + n, n)
        d(x + n, y + 2 * n, n)
        d(x + 2 * n, y, n)
        d(x + 2 * n, y + n, n)
        d(x + 2 * n, y + 2 * n, n)
    elif check == 1:
        one += 1
    elif check == 0:
        zero += 1
    else:
        mone += 1


d(0, 0, n)
print(mone)
print(zero)
print(one)