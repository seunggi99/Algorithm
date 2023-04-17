import sys
input = sys.stdin.readline

N, M = map(int,input().split())


d = [input().strip() for i in range(N)]
b = [input().strip() for j in range(M)]


db = sorted(list(set(d) & set(b)))

print(len(db))
for i in db:
    print(i)
