T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int,input().split())

    n = int(input())
    count = 0

    for _ in range(n):
        x,y,r = map(int,input().split())
        dis1 = (x1 - x)**2 + (y1 - y)**2
        dis2 = (x2 - x)**2 + (y2 - y)**2
        r2 = r**2

        if (dis1 < r2 and dis2 > r2) or (dis1 > r2 and dis2 < r2):
            count += 1

    print(count)

