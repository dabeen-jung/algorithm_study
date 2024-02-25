'''
[시뮬레이션] 로봇 청소기 (골5)

*goal : 작동이 중단될 때까지 청소하는 칸 갯수?

중단의 경우
1. 주변 (상하좌우)가 다 청소되었다면
2. 바라 본 방향을 유지 후 뒷칸으로 이동.
2-1. but 이동하려는 곳이 벽이면 => 중단단
'''
import sys
input = sys.stdin.readline

n,m = map(int, input().rstrip().split())
# 로봇 : (r,c) d방향(0북,1동,2남,3서)
r,c,d = map(int, input().rstrip().split())

room = [list(map(int, input().rstrip().split())) for _ in range(n)]
cnt = 0
#0:청소 x , 1: 청소함
visited = [[0] * m for _ in range(n)]

# 북동서남(0,1,2,3) 기준. '반시계' 방향 탐색이라
# 결과적으로는 서북동남 으로 탐색 예정
dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited[r][c] = 1 #처음은 방문처리
cnt = 1



while True:
    check = 0 # 4방향의 청소 여부 x

    for _ in range(4):
        # 반시계 방향으로 돌려서 탐색.
        d = (d+3)%4
        # 좌표도 바꿔줌
        nx = r + dx[d]
        ny = c + dy[d]

        #1. 청소 x방, 빈 방
        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0 and visited[nx][ny] == 0:
            visited[nx][ny] = 1  # 청소함
            cnt += 1  # 청소한 방 +=1
            r, c = nx, ny
            check = 1  # 4방향 중 청소를 1개라도 함
            break  # 방향 이동 후, 새로 4방향 탐색할거라 탈출


    # 2. 4방향 전부 탐색 && 전부 청소가 되어 있다.
    if not check:  #2-1. 후진했는데 벽이 있다=> 중단
         if room[r-dx[d]][c-dy[d]] == 1:
            print(cnt)
            break
         else:
            #2-2. 후진한 상태의 좌표로 조정.
            r,c = r-dx[d],c-dy[d]