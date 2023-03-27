a =int(input())

def check(n) :
    if n<0 :
        if n%2==0 :
            print('A')   
        else :
            print('B')
    else :
        if n%2==0 :
            print('C')
        else :
            print('D')
check(a)
