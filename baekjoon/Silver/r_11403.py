'''
[그래프] 경로 찾기 (실1)
가중치 x 방향 그래프 G
모든 정점에 대해서 i-> j 길이가 양수인 경로가 있는지 구하는

* 플루이드 와샬
- 거쳐가는 정점을 하나씩 다 설정을 하여 해당 정점을 기준으로 최단 거리를 구하도록 구성
→ 모든 쌍 간의 최단 거리를 구할 수 있음

goal: 인접행력 형식 출력

왜 틀렸는가? 처음 보는 개념 + bfs 이용 까먹음
'''

#플루이드 와샬 기법
import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int,input().rstrip().split())) for _ in range(N)]

# print(graph)

# [0,1], [1,2], [2,0] =>[1,0][2,1][0,2]
for k in range(N): # '반드시 경유할 점' (한 개는 있을거다)
    for i in range(N):
        for j in range(N):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for row in graph:
    print(' '.join(map(str,row)))


#[BFS]
# from collections import deque
#
# n = int(input())
# #입력받은 그래프
# graph = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0]*n for _ in range(n)] #출력할 행렬
#
# def bfs(start):
#     queue = deque([start])
#     # 방문처리 배열
#     check = [0 for _ in range(n)]
#
#     while queue:
#         v = queue.popleft()
#
#         #해당 i정점에서 다른 모든 정점으로 가는 경로가 존재하는가?
#         for i in range(n):
#             # 방문하지도 않았으면서, 해당 노드로 연결되는 간선이 존재한다?
#             # v=0 ,i =1 / que에서 v=1, i=0
#             #check=[0,1,0]
#             if check[i] == 0 and graph[v][i] == 1:
#                 queue.append(i)
#                 check[i] = 1
#                 visited[start][i] = 1
#         # print(visited)
# for i in range(n):
#     bfs(i)
#
# for i in visited:
#     print(*i)