'''
[우선순위 큐] 절댓값 힙 (실1)

1. 배열에 x (0이 아닌 정수) 넣음
2. x가 0이면, 열에 절댓값이 가장 작은 값 출력 > 해당 값을 배열에서 제거
-> 작은 값이 여러개면, 하나만 제거
'''

# from collections import deque
import heapq
import sys

input = sys.stdin.readline
n = int(input())

que = [] #빈 리스트
cnt = 0

for i in range(n):
    a = int(input())
    if a == 0:
        if not que: #우선순위 큐가 비여져있다.
            print("0")
        else:
            #가장 우선순위가 높은 항목 제거 & (abs(a),a) 중 a인 원래 값 출력
            print(heapq.heappop(que)[1])
    else:
        #(abs(x), x) 튜플의 형태로 que에 원소를 넣어줌
        # abs(a)가 작은 순(우선순위)으로 정렬됨
        heapq.heappush(que,(abs(a),a))
        # print(heapq)
        # print(que)
    cnt+=1