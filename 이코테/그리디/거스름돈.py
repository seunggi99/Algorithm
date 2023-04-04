money = [500,100,50,10]
N = 1260
count = 0

for i in money:
    count += N // i
    N  %= i

print(count)