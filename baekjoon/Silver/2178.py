#[dfs,bfs] 미로 탐색 (실버1)


def bfs(x,y):
    #1. 해당 인덱스 위치를 큐에 삽입
    que = deque()
    que.append((x,y))

    # 2. 큐가 빌 때까지 실행
    while que:
        # bfs 실행 (1. 맨 첫 값 제거 2.해당 값 관련한 노드 탐색 및 큐에 삽입)
        x,y = que.popleft()

        # 3. 현재위치에서 4방향으로 탐색 시작
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #2. 범위를 벗어나면 종료
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue #나머지 다른 방향까지 다 탐색해야함

            #2-1. 벽이면 무시
            if graph[nx][ny] == 0:
                continue

            #3. 탐색(1. 인접노드, 2. 방문한 적 x)이면 큐에 삽입 후 체크.
            if graph[nx][ny] == 1:
                # 이전 값보다 1증가시킴(=> 1이상 방문했다 check)
                graph[nx][ny] = graph[x][y] + 1
                #3-1. 큐에 위치 넣0어줌
                que.append((nx,ny))
    #4.그래프에 카운트 할 때마다 값을 넣음-> 해당 값 조회하면 끝
    #(0부터 셌으니 -1)
    return graph[n-1][m-1]


from collections import deque

n,m = map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

# print(graph)

#이동할 방향 [상,하,좌,우]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))