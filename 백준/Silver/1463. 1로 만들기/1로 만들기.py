import sys


N = int(sys.stdin.readline())

dp = [0, 0, 1, 1] # 1, 2, 3에 대한 값을 미리 씀

for i in range(4, N+1):
    dp.append(dp[i-1] + 1)
    if i % 3 == 0:
        dp[i] = min(1 + dp[i//3], dp[i])
    if i % 2 == 0:
        dp[i] = min(1 + dp[i//2], dp[i])

print(dp[N])