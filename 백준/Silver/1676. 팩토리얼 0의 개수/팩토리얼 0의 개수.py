import math

n = int(input())
n = math.factorial(n)
nlist = list(str(n))
count = 0
for i in nlist[::-1]:
    if i == '0':
        count +=1
    else:
        break
print(count)