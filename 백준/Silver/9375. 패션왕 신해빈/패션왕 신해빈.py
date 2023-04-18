import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    n = int(input())
    dict = {}

    for i in range(n):
        c = input().split()
        if c[1] in dict:
            dict[c[1]].append(c[0])
        else:
            dict[c[1]] = [c[0]]

    count = 1

    for i in dict:
        count *= (len(dict[i])+1)
    print(count-1)