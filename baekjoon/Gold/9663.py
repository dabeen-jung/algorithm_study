'''
[백트래킹] N-Queen (골4)

* goal:
1. 퀸끼리 '서로 공격할 수 없게' 놓는 '경우의 수'

* 퀸 특징
1. 수평 이동: 같은 행 어디던 (이동 가능)
2. 수직 이동: 같은 열 어디던 (이동 가능)
3. 대각선 이동
4. 공격:
    퀸이 이동하는 경로에서 '마주친 첫 번째 '상대 말'을 공격'
    - 다른 말을 뛰어 넘거나 / 자신의 말을 공격 할 수 x
5.
'''

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
graph = [[0] * N for _ in range(N)]
queen = [] #좌표 저장
cnt = 0 #경우의 수

#하,상,우,좌, 대각선 왼쪽, 대각선 오른족
dx = [0, 0, 1, -1, -1, 1, 1, -1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]

#2. 퀸들끼리 서로 공격하는지 여부 확인
def attack(x,y):
    que = deque((x,y))
    attack_ck = False #공격

    while que:
        x,y = que.popleft()

        for i in range(8):
            #행,열,대각선 두개
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            #if 내가 지나고 있을 때 상대가 하필 내 경로에 있음
            if graph[nx][ny] == 2:
                attack_ck = True
                break

            if graph[nx][ny] != 1:
                graph[nx][ny] = 1 #방문처리
                que.append((nx,ny))

    if attack_ck: #공격
        return False
    else:
        return True





def dfs(depth):
    global cnt

    if depth == N: #퀸이 N개 배치됨
        # 서로 공격할 수 없는지 여부 => ok =cnt+=1
        if attack(queen[0][0],queen[0][1]): #공격x
            cnt+=1
        return


    #1. 퀸을 배치,
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                continue

            queen.append([i,j])
            graph[i][j] = 2
            dfs(depth + 1)

            queen.pop() # 마지막 퀸 1개 제거
            graph[i][j] = 0 #방문여부 해지



dfs(0)
print(cnt)