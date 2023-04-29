import math

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    b = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(b)