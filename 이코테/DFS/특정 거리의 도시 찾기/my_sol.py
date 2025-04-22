from collections import deque


n,m,k,x = map(int,input().split())
way = list()

for i in range(m):
    way.append(list(map(int,input().split())))

graph = [[] for _ in range(m+1)]

for i,j in way:
    graph[i].append(j)

def bfs(graph,start,visited):
    queue = deque([start])

    visited[start] = True

    for _ in range(k+1):
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return queue


visited = [0] * (n+1)

result = list(bfs(graph,x,visited))

for i in result.sort():
    print(i)

