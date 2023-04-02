n = int(input())
line = []
for i in range(n):
    a = list(input())
    line.append(a)

for i in range(n):
    for n in range(len(line[i])):
        if line[i][0] != "(":
            print("NO")
        else:
                



print(line)