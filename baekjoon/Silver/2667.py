#[dfs,bfs] 단지번호붙이기 (실1)

# goal: 연결된(상하좌우) 집의 단지에 번호를 붙이고, 각 단지수별 집의 수 세기
#bfs?  상하좌우로 탐색하면서 집의 수를 세야 하니까 (분포도 조사)

#왜 몰랐을까?
# 1. bfs의 기본 코드 작성에 집착함
# 2. 간단한 예외사항 25줄처럼 문제에 따라 넣어줘야 되는 것을 생각 못함

from collections import deque


n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
res = []  #각 단지 내 집의 수
dx = [-1,1,0,0] #상하좌우
dy = [0,0,-1,1]

def bfs(x,y):
    cnt = 1
    #1.
    que = deque()
    que.append((x,y)) #위치 추가
    #젤 첨에 온 애도 큐에 넣은 후방문표시 체크
    graph[x][y] = 0

    #큐가 종료될 때까지
    while que:
        #2. x,y값 '큐'에서 추출
        x,y = que.popleft()

        # 3. 상하좌우로 탐색 시작
        for i in range(4):
            # print(que)
            nx = x + dx[i]
            ny = y + dy[i]

            # 패스1. 범위 벗어남
            if nx < 0 or ny < 0 or ny >= n or nx >= n:
                continue #패스
            #패스2. 벽임
            if graph[nx][ny] == 0:
                continue #패스

            if graph[nx][ny] == 1:
                # 방문표시 0, 위치값 큐에 넣음
                graph[nx][ny] = 0
                cnt+=1
                que.append((nx,ny))
    return cnt


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            res.append(bfs(i, j)) #누적 cnt 결과 res에 저장

res.sort()
print(len(res))
for i in res:
    print(i)