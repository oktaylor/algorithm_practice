import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

cnt = 0
def dfs(graph, v, visited): # dfs
    global cnt # 전역변수
    visited[v] = True # 방문
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)

N, M = map(int,input().split()) # 작업할 개수 N, 순서정보의 개수 M

graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int,input().split()) # A 하고 나서 B 할 수 있음
    graph[B].append(A)

X = int(input())

vstd = [False for _ in range(N+1)]

dfs(graph, X, vstd)

print(cnt)