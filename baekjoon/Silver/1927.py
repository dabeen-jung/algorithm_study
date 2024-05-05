'''
[우선순위 큐] 최소 힙 (실2)

1. x가 자연수-> 배열에 자연수 x를 넣는다.
2. x가 0이면 -> 배열의 가장 작은 값을 출력하고, 해당 값을 배열에서 제거
'''

import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = [] #우선순위 큐에 쓰일 list

for i in range(n):
    x = int(input())

    if x == 0:
        if not arr: #배열이 비어있는가?
            print("0")
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, x)