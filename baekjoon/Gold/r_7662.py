'''
[이진검색 트리] 이중 우선순위 큐 (골4)

*삭제(D 양수):우선순위가 가장 높은 데이터 1개 삭제
D 음수 : 가장 낮은 우선순위 데이터 1개 삭제
D인데 삭제할 값이 없으면 무시

*삽입 (I): 데이터 삽입

goal: 최종적으로 Q에 남은 데이터 중 최댓값과 최솟값만 출력
Q가 비였다면 'EMPTY'
'''
# import sys
# import heapq
#
# input = sys.stdin.readline

# Q = [] #우선순위 큐(최소힙)
# maxQ = []
# tc = int(input())
#
# for t in range(tc):
#     k = int(input())
#
#     for i in range(k):
#         a,n = map(str,input().split())
#
#         if a == 'I':
#             heapq.heappush(Q,int(n))
#             heapq.heappush(maxQ,-int(n)) #-를 넣어 삽입하면 (최댓값으로)
#         elif a == 'D':
#             if Q: #큐가 있어야만 삭제가 가능함
#                 if int(n) > 0:
#                     MAX = -heapq.heappop(maxQ) #- 넣어 삭제하면 최댓값 삭제
#                     Q.remove(MAX) #최소힙에서도 사라져야 함
#                 else:
#                     MIN = heapq.heappop(Q)
#                     # print(MIN)
#                     # print(Q)
#                     maxQ.remove(-MIN) #제거할 때도 마찬가지로 -해주자
#     if Q:
#         #최대 최소 출력
#         # 최대큐 중 가장 최댓값 , 최소 큐 중 가장 최솟값
#         print(f'{-heapq.heappop(maxQ)} {heapq.heappop(Q)}')
#     else:
#         print("EMPTY")
#
#     # Q.clear() #큐 초기화

# 정답 코드
import sys

input = sys.stdin.readline
import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    minQ, maxQ = [], []
    # 각 노드의 id에 대해 삭제되었는지 아닌지를 저장
    # 처음에는 아무 값도 없으므로 모두 삭제된 것으로 간주
    deleted = [True] * k
    for i in range(k):
        com, n = input().split()
        n = int(n)
        if com == 'I':
            heapq.heappush(minQ, (n, i))
            heapq.heappush(maxQ, (-n, i))
            deleted[i] = False
        else:
            if n == 1:
                # 삭제되지 않은 값 찾기
                # 삭제된 값은 힙에서 제거
                while maxQ and deleted[maxQ[0][1]]:
                    heapq.heappop(maxQ)
                if maxQ:
                    deleted[maxQ[0][1]] = True
                    heapq.heappop(maxQ)
            else:
                while minQ and deleted[minQ[0][1]]:
                    heapq.heappop(minQ)
                if minQ:
                    deleted[minQ[0][1]] = True
                    heapq.heappop(minQ)

    # 연산이 끝난 후 삭제된 값들 제거
    while minQ and deleted[minQ[0][1]]:
        heapq.heappop(minQ)
    while maxQ and deleted[maxQ[0][1]]:
        heapq.heappop(maxQ)

    if minQ and maxQ:
        print(-maxQ[0][0], minQ[0][0])
    else:
        print('EMPTY')