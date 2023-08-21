import sys
sys.setrecursionlimit(10**7) # python이 정한 최대 깊이를 더 깊게 변경해줌


n, m = map(int, sys.stdin.readline().split(' '))

# dfs(graph, recursion)
graph = [[]] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    f, t = map(int, sys.stdin.readline().split(' '))
    if graph[f] == []:
        graph[f] = [t]
    else:
        graph[f].append(t)
    if graph[t] == []:
        graph[t] = [f]
    else:
        graph[t].append(f)

def dfs(graph, i, visited):
    visited[i] = True
    for c in graph[i]:
        if not visited[c]:
            dfs(graph, c, visited)


cnt = 0
for v in range(1, len(visited)):
    if graph[v] == []: # 연결된 간선이 하나도 없다면
        visited[v] = True
        cnt += 1
    if visited[v] == False:
        dfs(graph, v+1, visited)
        cnt += 1


print(cnt)