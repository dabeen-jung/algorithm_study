#[bfs] 불! (골4)
# goal: 불에 타기 전 탈출 가능여부(IMPOSSIBLE)
# /탈출 가능하면-> 가장 빠른 탈출 시간
# 조건: 불은 네방향 확산, 탈출조건: 미로 가장자리 공간

import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0] #우,좌,하,상



# F 불이 퍼져나가는 것, J 이동을 세야함 => F이동과 J위치가 겹치면 즉시 탈락
#2. 불을 퍼트리는 함수 -> 불이 몇초안으로 붙었는지 누적됨 (fmaze)
def fbfs():
    while fque: #불은 계속 옮겨 붙음
        x,y = fque.popleft()

        for i in range(4): #상하좌우로 불이 퍼짐
            nx = x + dx[i]
            ny = y + dy[i]

            #범위 넘으면 break
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue

            #벽 or 이미 불이 지펴진 곳
            if maze[nx][ny] == '#' or fmaze[nx][ny] != 0:
                # print(fmaze[nx][ny])
                continue
            # 이 곳을 불 지피기까지 걸린 시간 누적
            fmaze[nx][ny] = fmaze[x][y] + 1
            fque.append((nx,ny))


#3. 사람이 도망가는 함수
def hbfs():
    while hque:
        x,y = hque.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 넘으면 출력(_성공적으로 탈출)
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                return print(hmaze[x][y])

            # 이미 벽이거나 도망간 곳임
            if hmaze[nx][ny] or maze[nx][ny] == '#':
                continue
            #해당 곳은 이미 불이 붙었음, 또한 애시당초 내가 도망오기 전부터 불난 곳임
            if fmaze[nx][ny] and hmaze[x][y] + 1 >= fmaze[nx][ny]:
                continue

            hmaze[nx][ny] = hmaze[x][y] + 1 # 불보다 사람이 더 빨리 도망옴-> 누적
            hque.append((nx,ny))
    return print("IMPOSSIBLE")




#미로(행,열) 갯수
R,C = map(int, input().rstrip().split())

# list()로 묶으면 문자열이더라도 각각의 문자가 별도의 요소로 분리된 리스트가 생성
# maze = [list(input().rstrip()) for _ in range(R)]
maze = []
fmaze = [[0]*C for _ in range(R)] #불 퍼지는 위치
hmaze = [[0]*C for _ in range(R)] #사람이 도망가는 위치(누적)

fque = deque()
hque = deque()

# 1. maze 입력값 저장 및 불과 현 위치 값 받기
for i in range(R):
    maze.append(list(input().strip()))
    for j in range(C):

        if maze[i][j] == 'F': #불?
            fque.append((i,j))
            fmaze[i][j] = 1
        elif maze[i][j] == 'J': #현위치
            hque.append((i,j))
            hmaze[i][j] = 1

fbfs()
hbfs()
