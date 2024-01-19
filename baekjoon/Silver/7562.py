#[bfs] 나이트의 이동 (실1)
#goal: 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동하는지 출력

import sys
from collections import deque
input = sys.stdin.readline

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]


def bfs(x,y):
    que = deque()
    que.append((x,y))

    while que:
        x, y = que.popleft()

        if x == g_x and y == g_y:
            return graph[x][y] - 1


        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            #2. 범위를 벗어나면 종료
            if nx<0 or nx >= n or ny <0 or ny>=n:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx,ny))





t_c = int(input())

for i in range(t_c):
    n = int(input()) #체스판 한 변 길이
    graph = [[0]*n for _ in range(n)]

    a,b = map(int, input().rstrip().split()) # 현 위치
    g_x,g_y = map(int, input().rstrip().split()) # 목표위치

    #시작점을 이미 밟고 있음 -> 끝나고 -1 해준다(횟수 세는거니까)
    graph[a][b] = 1
    # graph[g_x][g_y] = 1

    print(bfs(a,b))




