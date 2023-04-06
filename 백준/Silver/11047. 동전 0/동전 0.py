n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
count = 0
coin2 = sorted(coin,reverse = True)

for i in coin2:
    if k == 0:
        break
    elif k >= i:
        count += k//i
        k -= i * (k//i)

print(count)
