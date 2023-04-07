n = 1000 - int(input())

coin = 0

coin += n//500 
n -= 500*(n//500)

coin += n//100
n -= 100*(n//100)

coin += n//50
n -= 50*(n//50)

coin += n//10
n -= 10*(n//10)

coin += n//5 
n -= 5*(n//5)

coin += n

print(coin)