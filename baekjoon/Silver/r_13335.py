'''
[시뮬레이션] 트럭 (실1)
w: 다리의 길이
L : 다리의 무게 최대하중

주의: 트럭은 순서대로 가야함

1. 다리에 트러기 'w대'만큼 '동시에' 올라갈 수 있다.
goal: 모든 트럭이 다 건넌 최단시간
'''

import sys
input = sys.stdin.readline
from collections import deque

#트럭 수, 다리길이(동시에 올라올 수 있는 갯수), 버티는 무게
n,w,L = map(int, input().rstrip().split())
truck = list(map(int,input().rstrip().split()))

# 0.큐로 다리 구현
bridge = deque()
for _ in range(w):
    bridge.append(0)

sec = 0 #최단시간
idx = 0 #트럭 현 위치


# 1. 트럭이 다 출차할 때까지
while idx < n :
    sec+=1 # n회차
    bridge.popleft()

    # if 1) 차가 들어간다면, 무게(L)가 초과하는가
    if sum(bridge) + truck[idx] <= L:
        bridge.append(truck[idx])
        # print(bridge)
        idx+=1
    else:
        # if 2) 다리에 트럭 합류 x =>다리 위 트럭만 이동시킴
        # 0 7 -> 7 0으로 밀리는 것을 표현해주고자
        bridge.append(0)
# print(sec)

# 2. 1을 이어서 다리 위 트럭이 다 지나는 경우까지
while bridge:
    sec += 1
    bridge.popleft()

print(sec)