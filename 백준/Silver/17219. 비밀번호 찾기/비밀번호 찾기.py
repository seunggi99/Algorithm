N, M = map(int,input().split())

data = dict()
for _ in range(N):
    address, pw = input().split()
    data[address] = pw

for _ in range(M):
    ad = input()
    print(data[ad]) 
