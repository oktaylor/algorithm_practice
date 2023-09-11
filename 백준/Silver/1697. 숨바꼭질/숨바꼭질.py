import sys
from collections import deque

# n : 수빈, k : 동생
n, k = map(int, sys.stdin.readline().split())

def bfs(start, end):
    queue = deque([start])
    line = [0] * 100001
    while queue:
        loc = queue.popleft()
        if loc == end:
            return line[loc]
        
        for nex in [loc+1, loc-1, loc*2]:
            if -1 < nex < 100001:
                if line[nex]==0 or line[nex] > line[loc]+1:
                    queue.append(nex)
                    line[nex] = line[loc]+1
           

print(bfs(n, k))