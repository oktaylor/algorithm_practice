import sys
n = int(sys.stdin.readline()) # 문장의 개수

for _ in range(n):
    sent = list(map(str, sys.stdin.readline().rstrip().split(' ')))
    for word in sent:
        print(word[::-1], end=' ') # 단어 거꾸로 출력
    print('')
    