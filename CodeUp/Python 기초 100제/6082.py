a = int(input())

for i in range(1,a+1):
    tmp = i%10
    if tmp==3 or tmp==6 or tmp==9:
        print("X",end=" ")
    else:
        print(i,end=" ")

