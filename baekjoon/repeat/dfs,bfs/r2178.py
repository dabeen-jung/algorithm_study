'''
 미로 탐색
1:이동 가능한 칸, 0: 이동 x
goal: (1,1) 출발 ->(N,M) 위치로 이동시, 지나야 하는 최소 칸 수

왜 bfs인가? dfs는 시간초과가 걸릴 수 있고 모든 경로의 수를 셀 수 없으니
'''
from collections import deque


def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    while q:
        x,y = q.popleft()

        for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M :
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = 1 #이거 안 쓰고 graph 값으로 방문 여부 판단도 가능
                    q.append([nx,ny]) #cnt를 애초에 q에 함께 집어 넣는 것도 방법
                    graph[nx][ny] = graph[x][y] + 1


    return graph[N-1][M-1]



N,M = map(int, input().split())
visited = [[0] * M for _ in range(N)]
graph = [list(map(int,input())) for _ in range(N)]
print(bfs(0,0))

# for i in range(N):
#     for j in range(M):
#         print(graph[i][j], end =' ')
#     print()


#[테스트 -bfs 경로]
# import sys
# from collections import deque
#
# n, m = map(int, sys.stdin.readline().split())
# array = []
#
# for i in range(n):
#     array.append(list(map(int, sys.stdin.readline().strip())))
#
# d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#
#
# def bfs(y, x):
#     queue = deque()
#     queue.append((y, x))
#     while queue:
#         y1, x1 = queue.popleft()
#         for dx, dy in d:
#             if 0 <= y1 + dy < n and 0 <= x1 + dx < m:
#                 if array[y1 + dy][x1 + dx] == 1:
#                     array[y1 + dy][x1 + dx] = array[y1][x1] + 1
#                     queue.append((y1 + dy, x1 + dx))
#
#
# bfs(0, 0)
# for i in range(n):
#     for j in range(m):
#         print(array[i][j], end =' ')
#     print()
# print(array[n - 1][m - 1])