n = int(input())
list = list(map(int,input().split()))
x = 1000
for i in range(len(list)):
    if list[i] < x:
        x= list[i]

print(x)
