'''
queue
'''
import sys

n, w, l = map(int, sys.stdin.readline().split())
truck = list(map(int,sys.stdin.readline().split()))

time = 0
bridge = [] # 다리 위에 있는 트럭 하중
while truck: # 건너려는 트럭이 있다면
    time += 1
    if len(bridge) >= w: 
        bridge.pop(0)
    if sum(bridge) + truck[0] <= l:
        bridge.append(truck.pop(0))
    else:
        bridge.append(0)
print(time+w)