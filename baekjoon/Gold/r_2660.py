'''
[그래프] 회장뽑기 (골5)
점수: 다른 회원들과 '가까운 정도'에 따라


* 회장: 점수가 가장 작은 사람이 된다
goal: 회장의 점수, 회장이 될 수 있는 모든 이들 출력

?왜 r인가
점수를 어떻게 측정해야할지 구현하지 못했음.
이후 점수는 즉, 현재 노드와 - 가장 멀리떨어진 노드까지의 거리(깊이)
란 것을 알고 구현할 수 있었음
'''
from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    check = [0] * (n+1)
    q = deque([start])
    visited[start] = 1

    while q:
        x = q.popleft()

        for v in graph[x]:
            if visited[v] == 0:
                visited[v] = 1
                check[v] = check[x] + 1
                q.append(v)

    return check


n = int(input()) #회원 수
#1. 친구 관계 입력
graph = [[] for _ in range(n+1)]
while True:
    a,b = map(int,input().split())
    if a == -1 and b == -1:
        break
    else:
        graph[a].append(b)
        graph[b].append(a)


MIN = float('inf') #회장 후보 점수
chairman = [] #회장 후보들

#회원마다 돌릴거임
for i in range(1,n+1):
    visited = [0] * (n + 1)
    check = bfs(i)
    # print(check)
    depth = max(check)

    if MIN > depth:
        MIN = depth
        chairman = [i] #값이 변경될 수 있다.
        # print(chairman)

    elif MIN == depth: #회장 후보가 더 있다
        chairman.append(i)

#회장 점수(깊이), 회장후보 수 , 회장후보들
print(MIN,len(chairman))
print(' '.join(map(str,chairman)))



'''
플루티드 워셜 방법
- 가중치가 있는 그래프에서 최단거리를 구할 때 주로 이용
'''

# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())
# distance = [[sys.maxsize for  in range(n+1)] for  in range(n+1)]
# answer = []

# 그래프 입력
# while True:
#     s, e = map(int, input().split())
#
#     if s == -1 and e == -1: # 탈출
#         break
# #인접행렬로 입력 받아야 함 (인접 리스트 x)
#     distance[s][e] = 1
#     distance[e][s] = 1
#
#
# 인접 행렬 초기화
# for i in range(1, n+1):
#     distance[i][i] = 0
#
#
# 플로이드 워셜 - 최단거리로 구함(가중치 기준)
# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if distance[i][j] > distance[i][k] + distance[k][j]:
#                 distance[i][j] = distance[i][k] + distance[k][j]
#
# for i in range(1, n+1):
#     answer.append(max(distance[i][1:]))
#
# 점수, 후보 수 출력
# minval = min(answer)
# print(minval, answer.count(minval))
#
# 모든 후보 출력
# for i in range(n):
#     if answer[i] == minval:
#         print(i+1, end=' ')
