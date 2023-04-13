import sys
input = sys.stdin.readline

N, M = map(int,input().split())
num = list(map(int,input().split()))
sumlist=[0]
tmp = 0

for i in num:
    tmp += i
    sumlist.append(tmp)

for _ in range(M):
    ni, nj = map(int,input().split())

    print(sumlist[nj] - sumlist[ni-1])

