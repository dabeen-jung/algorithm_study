#[bfs] 적록색약 (골5) - Success
#적록색약 - 빨강과 초록의 구분을 x
#같은 색상 - 상하좌우 인접 => 같은 구역이다
#goal: 적록색약이 본 구역 수-(RG, B) / 아닌 사람이 본 구역수

import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
graph = [[]*(n) for _ in range(n)]

visited_gr = [[0]*n for _ in range(n)]
visited_nor = [[0]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

#여기서 color는 지금 어떤 color와 인접했는지를 보는 것
def bfs_gr (x,y, color):
    que = deque()
    que.append((x,y,color))
    visited_gr[x][y] = 1

    while que:
        x,y,color = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #범위 확인
            if nx < 0 or nx >= n or ny <0 or ny >=n:
                continue

            if color == 'R' or color == 'G':
                if (graph[nx][ny] == 'R' or graph[nx][ny] == 'G') and visited_gr[nx][ny] == 0:
                    visited_gr[nx][ny] = 1 #방문처리
                    que.append((nx,ny,color))
            elif color == 'B':
                if (graph[nx][ny] == 'B') and visited_gr[nx][ny] == 0:
                    visited_gr[nx][ny] = 1  # 방문처리
                    que.append((nx, ny, color))

# 적록 x 사람용
def bfs_nor (x,y, color):
    que_nor = deque()
    que_nor.append((x,y,color))
    visited_nor[x][y] = 1

    while que_nor:
        x,y,color = que_nor.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #범위 확인
            if nx < 0 or nx >= n or ny <0 or ny >=n:
                continue

            if color == 'R':
                if (graph[nx][ny] == 'R') and visited_nor[nx][ny] == 0:
                    visited_nor[nx][ny] = 1 #방문처리
                    que_nor.append((nx,ny,color))
            elif color == 'G':
                if (graph[nx][ny] == 'G') and visited_nor[nx][ny] == 0:
                    visited_nor[nx][ny] = 1 #방문처리
                    que_nor.append((nx,ny,color))

            elif color == 'B':
                if (graph[nx][ny] == 'B') and visited_nor[nx][ny] == 0:
                    visited_nor[nx][ny] = 1  # 방문처리
                    que_nor.append((nx, ny, color))




#1. 입력값 받기
for i in range(n):
    arr = input().rstrip()
    for v in arr:
        graph[i].extend(v)
# print(graph)


cnt_nor = 0
# 2-1. 적록색약 아닌 사람이 그래프 봤을 때
for i in range(n):
    for j in range(n):
        if visited_nor[i][j] == 0:
            # print("000이다" ,graph[i][j])
            #인접해 있는 묶음들을 다 세보고 나옴-> bfs함수로
            # 이제 없으면 나와서 다음꺼를 찾음
            bfs_nor(i,j,graph[i][j])
            cnt_nor += 1
print(cnt_nor)

cnt = 0
#2-2. 적록색약이 그래프를 봤을 때
for i in range(n):
    for j in range(n):
        if visited_gr[i][j] == 0:
            # print("0이다" ,graph[i][j])
            bfs_gr(i,j,graph[i][j])
            cnt+=1
print(cnt)