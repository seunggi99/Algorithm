n = list(map(int,input()))

h = len(n) // 2

sum1 = 0
sum2 = 0

for i in range(h):
    sum1 += n[i]
for i in range(h,len(n)):
    sum2 += n[i]

if sum1== sum2 :
    print("LUCKY")
else:
    print("READY")


