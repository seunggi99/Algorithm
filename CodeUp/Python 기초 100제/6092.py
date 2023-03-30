n = int(input())

list = list(map(int,input().split()))

list2 =[]
for i in range(1,24):
    list2.append(list.count(i))

for i in range(0,23):
    print(list2[i] , end=" ")
