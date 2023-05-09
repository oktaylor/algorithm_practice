'''
(-)부호를 기준으로 괄호를 치자
'''
import sys

x = sys.stdin.readline().rstrip().split('-') # (-) 부호 기준으로 자름
cal = []
for i in x:
    plus = i.split('+')
    a = 0
    for j in plus:
        a += int(j)
    cal.append(a)

result = cal[0]
for i in range(1, len(cal)):
    result -= cal[i]
print(result)