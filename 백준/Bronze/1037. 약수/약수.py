N = int(input())
a = map(int,input().split())
min = 99999999
max = 1

for i in a:
    if i < min:
        min = i

    if i > max:
        max = i

print(min*max)