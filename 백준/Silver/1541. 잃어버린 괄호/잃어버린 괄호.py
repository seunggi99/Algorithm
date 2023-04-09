def plus(k):
    s = 0
    pl = list(map(int,k.split('+')))
    
    for i in pl:
        s += i
    return s


sik = list(input().split('-'))

sum = plus(sik[0])

for i in range(1,len(sik)):
    sum -= plus(sik[i])

print(sum)


