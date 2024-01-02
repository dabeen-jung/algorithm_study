# [큐] 카드2 (실버4)
# goal: 마지막 카드 한 장이 남을 때 무엇인가
# rule: 제일 위 카드는 버림, 그 다음 제일 위 카드를 제일 아래로

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
deq = deque(i+1 for i in range(n))

while deq:
    # 1인경우도 생각해야함
    if n != 1:
        deq.popleft()
    if len(deq) == 1:
        break
    deq.append(deq.popleft())

print(deq[0])