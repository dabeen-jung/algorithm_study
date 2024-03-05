'''
[시뮬레이션] 주사위 굴리기 (골4)
맨처음: 주사위 윗면은 1, 바닥면은 6임
동(1), 서(2), 북(3), 남(4)

1. 주사위를 굴림
2. 이동한 지도 칸의 '정수'가 0이면, '주사위 바닥면'에 쓰인 숫자-> 지도칸에 복사됨
2-1. 정수가 0이 x면 ?,  '지도칸'의 수가 -> 주사위 바닥면으로 복사, 지도칸은 0이된다.

! 명령이 바깥으로 이동시킨다? => 무시 continue

goal:
이동할 때마다 주사위의 윗 면에 쓰인 숫자를 출력해라(바깥으로 나가면 출력하면 안됨)
'''

import sys
input = sys.stdin.readline


# 지도위에 윗면 1, 동쪽 3인 상태로 놓여있음 기준으로 굴리기
def roll(move):
    if move == 1: # 동쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3],dice[4], dice[5] \
     = dice[3], dice[1],dice[0], dice[5], dice[4], dice[2] # 주사위 변화 4 2 1 6 5 3

    elif move == 2: # 서쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] \
    = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3] # 주사위 변화 3 2 6 1 5 4

    elif move == 3: # 북쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] \
    = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1] # 주사위 변화 5 1 3 4 6 2

    elif move == 4: # 남쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] \
    =  dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]  # 주사위 변화 2 6 3 4 1 5


#지도 크기(N,M), 주사위좌표(x,y), 명령의 갯수(k)
N,M,x,y,k = map(int,input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
dice_move = list(map(int, input().split())) #주사위 이동명령(4방향 중 1개 제시)
dice = [0,0,0,0,0,0]


#동(1)서(2)북(3)남(4) 순
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


for i in dice_move:
    #이동한 거리가 범위를 넘지 않아야 함
    if 0 <= x + dx[i-1] < N and 0 <= y + dy[i-1] < M:
        x = x + dx[i-1]
        y = y + dy[i-1]

        roll(i) #이동방향(1,2,3,4 중 1개)

        if graph[x][y] == 0: #이때 지도칸이 0이면?
            graph[x][y] = dice[5] # 주사위 바닥부분(5번인덱스) -> 지도에 복사함

        elif graph[x][y] != 0: #0이 아니라면?
            dice[5] = graph[x][y]
            graph[x][y] = 0
        print(dice[0]) #주사위 윗부분은 1번 idx로는 0임.
