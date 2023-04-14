import sys
input = sys.stdin.readline
M = int(input())
S = [0]*20

for _ in range(M):
    order = input().split()
    if order[0] == 'add':
        S[int(order[1])-1] = int(order[1])
    elif order[0] == 'remove':
        S[int(order[1])-1] = 0
    elif order[0] == 'check':
        if S[int(order[1])-1] == 0:
            print(0)
        else:
            print(1)
    elif order[0] == 'toggle':
        if S[int(order[1])-1] == int(order[1]):
            S[int(order[1])-1] = 0
        else:
            S[int(order[1])-1] = int(order[1])
    elif order[0] == 'all':
        S = [i for i in range(1,21)]
    elif order[0] == 'empty':
        S = [0]*20