'''
[우선순위 큐] 카드정렬하기 (골4)
A,B
(a+b)+((a+b)+c) = ?
=> a+b를 최소한으로 만들어라

"아쉽게 접근을 잘못한 문제"
'''

import sys
import heapq
input = sys.stdin.readline

N= int(input())
q = []

for i in range(N):
    num = int(input())
    heapq.heappush(q,num)

goal = 0 # 누적합

while len(q) > 1: #큐 원소가 1개가 남기 전까지 돌림
    #현재 큐에 공존하는 최솟값 2개 추출
    v1 = heapq.heappop(q)
    v2 = heapq.heappop(q)

    two_sum = v1 + v2
    goal += two_sum

    #합친 묶음은 다시 우선순위 큐에 넣어줌
    # ㄴ> 즉, "가장 작은 값의 묶음끼리" 합해줄 수 있다
    heapq.heappush(q,two_sum)

print(goal)
