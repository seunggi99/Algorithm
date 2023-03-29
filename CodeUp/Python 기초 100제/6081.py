a = input()
x = int(a,16)
for i in range(1, 16):
    print(a+"*"+format(i,'X')+"="+format(i*x,'X'))
