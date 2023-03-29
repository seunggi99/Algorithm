a, b, c = map(int,input().split())

for i in range(1,b+1):
    if a*i%b==0:
        d = a*i
        break

for i in range(1,c+1):
    if d*i%c==0:
       e = d*i
       break
print(e)
