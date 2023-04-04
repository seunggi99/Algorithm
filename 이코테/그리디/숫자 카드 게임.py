N, M =  map(int,input().split())

x = []
num = []

for i in range(N):
    x.append (list(map(int, input().split())))
    num.append(min(x[i]))

print(max(num))