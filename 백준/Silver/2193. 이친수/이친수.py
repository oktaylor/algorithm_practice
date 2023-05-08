'''
이전 이친수 + 이전 이친수에서 0으로 끝나는 수
'''
import sys

n = int(sys.stdin.readline())

bf = [0, 1, 1]
zero_end = [0, 0, 1]
for i in range(3, n+1):
    bf.append(bf[i-1] + zero_end[i-1])
    zero_end.append(bf[i-1])

print(bf[n])

