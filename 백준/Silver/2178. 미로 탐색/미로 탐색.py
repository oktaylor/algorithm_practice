import sys
from collections import deque


# 우선되야할 것 : 오른쪽, 아래 방향으로 가는 것
# matrix의 값을 이동횟수로 만들기

n, m = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]


def bfs(matrix, x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        if x+1 < m and matrix[y][x+1] == 1: # 오른쪽 이동
            queue.append((x+1, y))
            matrix[y][x+1] += matrix[y][x]
        if y+1 < n and matrix[y+1][x] == 1: # 아래로 이동
            queue.append((x, y+1))
            matrix[y+1][x] += matrix[y][x]
        if x-1 > -1 and matrix[y][x-1] == 1:
            queue.append((x-1, y))
            matrix[y][x-1] += matrix[y][x]
        if y-1 > -1 and matrix[y-1][x] == 1:
            queue.append((x, y-1))
            matrix[y-1][x] += matrix[y][x]
        if x == m-1 and y == n-1:
            return matrix[y][x]
    return matrix[y][x]


print(bfs(mat, 0, 0))