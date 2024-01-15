#[dfs, bfs] 안전영역 (실1)
# 안전한 영역 구하기
# 안전영역: 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접한 영역

# BFS로 풀어야 함
# 가까운 영역을 전부 탐색해서 안전영역의 갯수를 세야함


from collections import deque
import sys
input = sys.stdin.readline


#3. bfs 함수 실행
def bfs(x,y, high):
    que = deque()
    que.append((x,y))
    visited[x][y] = 1 #방문

    while que:
        x,y = que.popleft()

        #상하좌우 방향으로 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프를 영역 밖으로 벗어나지 않게
            if nx <0 or ny < 0 or ny>=n or nx >= n:
                continue

           # 현재 물의 수심과 비교, 방문 전적 x 면 => 동작
            if graph[nx][ny] > high and visited[nx][ny] == 0:
                visited[nx][ny] = 1 #방문처리 함함
                que.append((nx,ny))



# 1. 입력값 받기
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
high = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] > high: #최대 높이값 저장
            high = graph[i][j]

dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1]


MAX = 0
# 2. 수심이 달라질 때마다 달라지는 안전영역 갯수 비교
for t in range(high):
    visited = [[0] * n  for _ in range(n)]
    cnt = 0 #안전 영역 갯수

    for i in range(n):
        for j in range(n):
            # 해당 칸을 방문한 전적 x, 해당 칸은 수심보다 높음 => bfs실행
            #bfs 실행으로 인접 영역들을 visited[] 체크해줌
            if graph[i][j] > t and visited[i][j] == 0:
                bfs(i,j,t)
                cnt+=1
    # 4. 해당 수심의 안전영역과 & 현재까지 가장 컸던 안전영역 갯수를 비교
    if MAX < cnt:
        MAX = cnt

print(MAX)