T = int(input())
for _ in range(T):
    N = int(input())
    z,o=1,0 
    for i in range(N):
        z,o = o,z+o
    print(z,o)