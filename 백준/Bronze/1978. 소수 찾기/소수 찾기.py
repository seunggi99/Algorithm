n = int(input())
num = map(int, input().split())
s = 0
for i in num:
    error = 0
    if i > 1 :
        for m in range(2, i):  
            if i % m == 0:
                error += 1  
        if error == 0:
            s += 1  
print(s)