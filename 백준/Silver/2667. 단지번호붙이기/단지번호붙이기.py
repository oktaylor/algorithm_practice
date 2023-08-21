import sys


n = int(sys.stdin.readline())
vilage = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
cnt = 0

def dfs(matrix, x, y):
    matrix[y][x] = 0
    global cnt
    cnt += 1
    if x-1 > -1 and matrix[y][x-1] == 1:
        dfs(matrix, x-1, y)
    if x+1 < n and matrix[y][x+1] == 1:
        dfs(matrix, x+1, y)
    if y-1 > -1 and matrix[y-1][x] == 1:
        dfs(matrix, x, y-1)
    if y+1 < n and matrix[y+1][x] == 1:
        dfs(matrix, x, y+1)


count = [] # 단지 내 가구 수
vil = 0 # 단지 개수
for i in range(n): # y
    for j in range(n): # x
        if vilage[i][j] == 1:
            dfs(vilage, j, i)
            count.append(cnt)
            cnt = 0
            vil += 1


print(vil)
count.sort()
for i in count:
    print(i)
