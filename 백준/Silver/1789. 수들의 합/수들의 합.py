n = int(input())
s = 0
sum = 0
while sum <= n:
    s += 1
    sum += s
print(s-1)