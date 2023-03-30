n = int(input())
list = list(map(int,input().split()))

for i in list[::-1]:
    print(i,end=" ")
