#[bfs] 토마오 (골5)

# 익은 토마토 주변 상하좌우 앞!뒤! 가 익는다
#goal: 며칠이 지나면 다 익을지 (최소 일수를 출력하라),
# => 만일 첨부터 익어잇다면 0, 모두 익을리가 없다면 -1
#=> 결과적으로 모든 결과가 -1,1만 공존해야 함 / 그게 안되면 출력 -1

#정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토,
# 정수 -1은 토마토가 없는 칸
# => 0만 영향 받음
import sys
input = sys.stdin.readline

from collections import deque
que = deque()

#상하좌우, 앞 뒤
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1 , -1]
dk = [1,-1, 0, 0, 0, 0]

def bfs():
    while que:
        k,x,y = que.popleft()

        for i in range(6): #앞뒤상하좌우
            nk = k + dk[i]
            nx = x + dx[i]
            ny = y + dy[i]

            # 패스 1. 범위 벗어남
            if nx <0 or ny < 0 or nk <0 or ny >= m or nx >=n or nk >= h:
                continue

            if graph[nk][nx][ny] == 0:
                graph[nk][nx][ny] = 1 + graph[k][x][y]
                #중요) + graph[k][x][y] 의 의미
                #이것을 통해 현재 며칠이나 지난건지 의미 파악
                que.append((nk,nx,ny))



# 가로,세로, 높이
m, n, h = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(h)]

#3중 리스트 값 입력받기
for i in range(h):
    for j in range(n):
        graph[i][j] =list(map(int, input().split()))

# print(graph)

# 2. 큐에 위치 넣기 (1들을 찾아 넣을 것)
# 즉, que로 인해 주변이 영향을 받을 것이니 ->영향을 주는 위치를 넣는다
for i in range(h):
    for j in range(n):
        for k in range(m):
            # print(graph[i][j][k])
            if graph[i][j][k] == 1: #익은 애들을 큐에 넣어줌
                que.append((i,j,k)) #높이, 가로(행), 세로


# 3. bfs 함수 실행
# 큐를 돌면서 1의 인접영역에 영향을 줌
bfs()



# 4. 일자가 얼마나 걸릴지
# - 하나라도 0이 존재하면 실패임=> 무슨 일이 있어도 장애물(-1) 땜에 익을 수가 없음
# - 그래프 안의 값은 누적됨 => 매일 누군가를 거친 후 익음 (하루가 지남 (1획 돌았다))
cannot = False
day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):

            if graph[i][j][k] == 0:
                cannot = True
            day = max(day,graph[i][j][k])

if cannot:
    print(-1)
else:
    print(day -1)



# for i in range(h):
#     for j in range(n):
#         for k in range(m):
#             print(graph[i][j][k], end = ' ')
#         print()
#     print()


