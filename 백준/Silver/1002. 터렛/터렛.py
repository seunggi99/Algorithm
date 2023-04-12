import math

n = int(input())
for i in range(n):
    tur = list(map(int,input().split()))
    dis = math.sqrt((tur[0]-tur[3])**2 + (tur[1]-tur[4])**2)
    r = tur[2] + tur[5]
    r2 = abs(tur[2] - tur[5])

    if dis == 0 and r2 == 0:
        print(-1)
    elif dis == r or dis == r2:
        print(1)
    elif r2< dis < r:
        print(2)
    else:
        print(0)