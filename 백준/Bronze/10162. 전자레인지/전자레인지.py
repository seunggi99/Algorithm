t = int(input())
a = [300, 60, 10]
time = [0,0,0]
for i in range(3):
    time[i] = t//a[i]
    t -= ((t//a[i]) * a[i])
    
if t > 0:
    print(-1)
else:
    for i in range(3):
        print(time[i], end = " ")