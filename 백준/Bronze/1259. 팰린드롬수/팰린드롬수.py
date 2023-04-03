while 1:
    a = input()
    if int(a) == 0:
        break
    elif a[::-1] == a:
        print('yes')
    else:
        print('no')