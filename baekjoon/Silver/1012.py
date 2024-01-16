#[dfx,bfs] 유기농 배추 (실2)

# 지렁이 특) 상하좌우에 위치한 배추도 보호해줌
# goal: 지렁이 1마리가 커버치는걸 고려하더라도 총 필요한 지렁이가 얼마일까?
# 즉, 1의 묶음이 몇 개인가
# 1: 배추 ㅇ, 0: 배추x

from collections import deque

t_c = int(input())

def bfs(x,y):
    que = deque()
    que.append((x,y))
    graph[x][y] = 0 #방문처리

    while que:
        x,y = que.popleft()

        for i in range(4): #상하좌우
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append((nx,ny))


dx = [1,-1,0,0]
dy = [0,0,1,-1]


for t in range(t_c):
    m, n, k = map(int, input().split())  # 가로,세로,배추 갯수
    graph = [[0] * n for _ in range(m)]

    for i in range(k):
        #배추 위치(x,y)
        x,y = map(int, input().split())
        graph[x][y] = 1

    # 함수 실행
    # print(graph)

    cnt = 0
    for j in range(m):
        for l in range(n):
            if graph[j][l] == 1:
                bfs(j,l)
                cnt+=1
    print(cnt)