import sys

N = int(sys.stdin.readline())

stack = []
count = 0

for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == "pop":
      if count == 0 :
          print(-1)
      else:
          print(stack[count-1])
          del stack[count-1]
          count -= 1
    elif order[0] == "size":
      print(count)
    elif order[0] == 'empty' :
      if count == 0:
        print(1)
      else:
        print(0)
    elif order[0] == "top":
      if count == 0:
        print(-1)
      else:
        print(stack[count-1])
    elif order[0] == "push":
      stack.append(order[1])
      count += 1