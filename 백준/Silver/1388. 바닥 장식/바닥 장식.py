import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

def dfs(y, x):
    if graph[y][x] == '-':
        graph[y][x] = 0 # 방문처리
        for i in [-1, 1]:
            if 0 <= x+i < m and graph[y][x+i] == '-':
                dfs(y, x+i)

    elif graph[y][x] == '|':
        graph[y][x] = 0 # 방문처리
        for i in [-1, 1]:
            if 0 <= y+i < n and graph[y+i][x] == '|':
                dfs(y+i, x)

cnt = 0
for y in range(n):
    for x in range(m):
        if graph[y][x] != 0:
            dfs(y, x)
            cnt += 1
print(cnt)