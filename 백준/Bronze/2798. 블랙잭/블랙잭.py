import sys

'''
for문으로 전체 케이스를 확인해봄
'''

n, m = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))

max = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= m and sum > max:
                max = sum
print(max)