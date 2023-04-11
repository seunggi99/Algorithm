n = int(input())
w = []
for i in range(n):
    w.append(int(input()))
w.sort()
result = 0
for i in range(n):   
    sum = w[i] * (n - i)

    if sum > result:
        result = sum

print(result)
