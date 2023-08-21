'''
ref : https://velog.io/@tks7205/dfs%EC%99%80-bfs%EB%A5%BC-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-%EC%97%AC%EB%9F%AC%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95-in-python

<인접 행렬>
특정 노드 간의 연결 정보 확인

<인접 리스트>
모든 연결 정보 확인

<dfs의 4가지 구현 방법>
1. 인접행렬, stack 자료구조
2. 인접행렬, 재귀함수
3. 인접리스트, stack 자료구조
4. 인접리스트, 재귀함수
'''


import sys
from collections import deque


# n, m, v = map(int, sys.stdin.readline().split(' '))
# matrix = [[0] * (n+1) for _ in range(n+1)] # node의 idx가 1부터 시작하기때문에 크기 1씩 추가
# visited = [False] * (n+1)

# for _ in range(m): # 간선의 개수만큼 존재
#     f, t = map(int, sys.stdin.readline().split(' '))
#     matrix[f][t] = matrix[t][f] = 1


# # 1. 인접행렬, stack 자료구조
# def dfs(matrix, i, visited):
#     stack = [i]
#     while stack:
#         value = stack.pop()
#         if not visited[value]: # visited[value]의 값이 False라면
#             print(value, end=' ') 
#             visited[value] = True # 방문한 자리 표시
#         for c in range(len(matrix[value])-1, -1, -1): # stack이기 때문에 거꾸로 집어넣어줘야 작은 수 부터 출력됨
#             if matrix[value][c] == 1 and not visited[c]: # value와 c가 이어져있고, c를 방문하지 않았다면,
#                 stack.append(c)


# # 2. 인접행렬, 재귀함수
# def dfs(matrix, i, visited):
#     visited[i] = True # 방문한 자리 표시
#     print(i, end=' ')
#     for c in range(len(matrix[i])):
#         if matrix[i][c] == 1 and not visited[c]: # value와 c가 이어져있고, c를 방문하지 않았다면,
#             dfs(matrix, c, visited)

#############################################################

n, m, v = map(int, sys.stdin.readline().split(' '))
graph = [[]] * (n+1)
visited = [False] * (n+1)

for _ in range(m): # 간선의 개수만큼 존재
    f, t = map(int, sys.stdin.readline().split(' '))
    if graph[f] == []:
        graph[f] = [t]
    else:
        graph[f].append(t)
    if graph[t] == []:
        graph[t] = [f]
    else:
        graph[t].append(f) 

# # 3. 인접리스트, stack 자료구조
# def dfs(graph, i, visited):
#     stack = [i]
#     while stack:
#         value = stack.pop()
#         if not visited[value]:
#             print(value, end=' ')
#             visited[value] = True
#         for j in graph[value]:
#             if not visited[j]:
#                 stack.append(j)

# for i in graph: # stack이기 때문에 거꾸로 집어넣어줘야 작은 수 부터 출력됨
#     i.sort(reverse=True)


# 4. 인접리스트, 재귀 함수
def dfs(graph, i, visited):
    visited[i] = True
    print(i, end=' ')
    for j in graph[i]:
        if not visited[j]:
            dfs(graph, j, visited)

for i in graph:
    i.sort()

dfs(graph, v, visited)

print()

'''
<bfs의 2가지 구현 방법>
1. 인접행렬, queue 자료구조
2. 인접리스트, queue 자료구조
'''
# # 1. 인접행렬, queue 자료구조
# n, m, v = map(int, sys.stdin.readline().split(' '))
# matrix = [[0] * (n+1) for _ in range(n+1)]
# visited = [False] * (n+1)

# for _ in range(m):
#     f, t = map(int, sys.stdin.readline().split(' '))
#     matrix[f][t] = matrix[t][f] = 1


# def bfs(matrix, i, visited):
#     queue = deque()
#     queue.append(i)
#     while queue:
#         value = queue.popleft()
#         if not visited[value]:
#             visited[value] = True
#             print(value, end=' ')
#             for c in range(len(matrix[value])):
#                 if matrix[value][c] == 1 and not visited[c]:
#                     queue.append(c)

# 2. 인접 리스트, queue 자료구조
# n, m, v = map(int, sys.stdin.readline().split(' '))
# graph = [[]] * (n+1)
visited = [False] * (n+1)

# for _ in range(m):
#     f, t = map(int, sys.stdin.readline().split(' '))
#     if graph[f] == []:
#         graph[f] = [t]
#     else:
#         graph[f].append(t)
#     if graph[t] == []:
#         graph[t] = [f]
#     else:
#         graph[t].append(f)

def bfs(graph, i, visited):
    queue = deque()
    queue.append(i)
    while queue:
        value = queue.popleft()
        if not visited[value]:
            visited[value] = True
            print(value, end=' ')
            for j in graph[value]:
                queue.append(j)

bfs(graph, v, visited)