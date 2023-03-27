a,b,c=map(int,input().split())
q = a if(a<=b) else b
print(q if(q<=c) else c)