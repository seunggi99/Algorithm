N = int(input())
num = list(map(int,input().split()))
numlist3 = [[1,2,3],[1,2,4],[1,3,5],[1,4,5],[2,3,6],[2,4,6],[3,5,6],[4,5,6]]
def check2(num):
    min = 999999
    for i in range(6):
        for n in range(i+1,6):
            if i+n != 5:
                if min > num[i] + num[n]:
                    min = num[i] + num[n]
    return min

def check3(num):
    min = 999999

    for i in numlist3:
        if min > num[i[0]-1] + num[i[1]-1] + num[i[2]-1]:
            min = num[i[0]-1] + num[i[1]-1] + num[i[2]-1]
        
    return min

if N == 1:
    cn = sorted(num)
    print(sum(cn) - cn[5]) 
else:
    a = check3(num)*4
    b = check2(num) * (4*(N-1) + 4*(N-2))
    c = min(num) * ((N-2)*(N-1)*4 + (N-2)*(N-2))
    print(a+b+c) 