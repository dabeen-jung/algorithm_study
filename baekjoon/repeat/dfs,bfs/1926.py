'''
그림
그림의 기준은 1임

*dfs를 한 이유?
깊이 위주로 이어지는 1을 다 셀테니까

갯수: dfs가 완전히 끝났을 때 +1
큰 넓이: 완전히 끝났을 때 최대 크기 비교
goal: 그림 갯수, 가장 큰 넓이
'''


'''
1. 방문처리 배열을 만든다
2. for 문을 돌리면서 값을 확인 
    - 방문한 적 x & 1인배열
'''
from collections import deque

dx = [0,1,0,-1] #우,하,좌,상
dy = [1,0,-1,0]

def dfs(x,y):
    #초기설정
    q = deque()
    q.append((x,y))
    wide = 1 #기본값 넓이
    graph[x][y] = 0 #방문처리함

    while q:
        # dfs라 스택처럼 생각(위에서부터 빼야함)
        # 이를 기준으로 '상하좌우'를 탐색시작
        x,y = q.pop()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = 0
                wide += 1 #넓이 늘어남
    return wide


#행,열
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
MAX = 0
cnt = 0 #그림갯수

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            MAX = max(dfs(i,j), MAX) #넓이 갱신
            cnt += 1 #그림 갯수

print(cnt)
print(MAX)