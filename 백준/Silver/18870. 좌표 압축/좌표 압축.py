import sys
input = sys.stdin.readline

N = int(input())

x = list(map(int,input().split()))
newx = sorted(set(x))
c = {newx[i]:i for i in range(len(newx))}

for i in x:
    print(c[i],end=" ")

