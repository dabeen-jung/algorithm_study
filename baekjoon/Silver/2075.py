'''
[우선순위 큐] N번째 큰 수 (실2)

모든 수는 자기 위에 숫자보다 큼
'''

import sys
import heapq

input = sys.stdin.readline
N = int(input())

#[메모리 초과]
# arr.sort(reverse=True)
#
# print(arr[N-1])

q = []

for i in range(N):
    a = list(map(int, input().split()))

    for v in (a):
        if i == 0: #첫 행은 그대로 넣어준다.
            heapq.heappush(q,v)
        else: #나머지 행들 비교
            if q[0] < v:
            #현재 우선순위 큐의 첫행보다 크다? => 큰 값 갱신
                heapq.heappush(q,v)
                heapq.heappop(q) #첫행 삭제

#[N위,4위,3위,1위]
print(q[0])