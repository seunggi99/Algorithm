n = int(input())
dis = list(map(int,input().split()))
price = list(map(int,input().split()))
result = 0

i = 0
while len(dis) > 0:
        count = 0

        result += price[i] * dis[0]
        count += 1
        del(dis[0])        

        if price[i] < price[i+1]:
            for m in range(i+1,n):
                if len(dis) == 0:
                    break
                elif price[i] >= price[m]:
                    break
                else:
                    result += price[i] * dis[0]
                    count += 1
                    del(dis[0])

        i += count

print(result)                         
