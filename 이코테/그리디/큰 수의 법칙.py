N, M, K = map(int,input().split())
a = list(map(int, input().split()))
sum = 0
count = 0
a.sort()

num1 = a[N-1]
num2 = a[N-2]

for i in range(M):
    if count == K:
        sum += num2
        count = 0
    else:
        sum += num1
        count += 1

print(sum)