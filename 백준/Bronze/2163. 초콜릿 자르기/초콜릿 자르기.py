import sys
input = sys.stdin.readline()

n, m = map(int, input.split()) # 입력 n, m

print(m * n - 1) # (n-1) + n(m-1)
