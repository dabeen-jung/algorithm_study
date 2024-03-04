'''
[시뮬레이션] 톱니바퀴 (골5)

goal:
회전의 영향을 받는 톱니바퀴가 최종으로 어떤 상태인지 구해라
=> 4개의 톱니바퀴의 각 점수들의 합을 출력해라
'''

from collections import deque
import sys
input = sys.stdin.readline

gear = [deque(list(map(int, input().rstrip()))) for _ in range(4)]

k = int(input())


# 1. 회전 입받기 [톱니바퀴 번호, 방향(1:시계, 0:반시계)]
for _ in range(k):
    r = [] #처음 톱니 상태 저장
    for i in range(4):
        # 톱니바퀴 별로 처음 상태 저장 (2번,6번 idx의 극을 기억)
        r.append([gear[i][6], gear[i][2]])

    n,direct = map(int, input().rstrip().split())
    n = n-1

    #2. 번호 확인 후 회전함수 돌리기
    # (내 기준 왼쪽에 있는 톱니들 돌리기)
    if n != 0:
        for i in range(n,0,-1):

            # 내 기준 왼쪽 톱니랑 비교
            # 2-1. 극이 다름(왼쪽 톱니, 나 회전)
            if r[i][0] != r[i-1][1]:
                # 2-1-1. 나를 기준으로 짝수에 위치 & 극이 다름 => 나와 방향이 같다
                if (n-(i-1)) % 2 == 0:
                    gear[i-1].rotate(direct) #나와 방향 똑같음

                #2-1-2. 홀수에 위치 & 극이 다름 => 방향 다름
                elif (n-(i-1)) % 2 != 0:
                    gear[i - 1].rotate(direct * -1)

            elif r[i][0] == r[i-1][1]: #극이 같음(나만 회전)
                break #탈출 후 따로 돌려줄거임

    #오른쪽에 있는 톱니들 돌리기
    if n != 3:
        for i in range(n,3):
            # 2-1. 극이 다름(오른쪽 톱니, 나 회전)
            if r[i][1] != r[i+1][0]:
                # 2-1-1. 나를 기준으로 짝수에 위치 & 극이 다름 => 나와 방향이 같다
                if (n - (i + 1)) % 2 == 0:
                    gear[i + 1].rotate(direct)  # 나와 방향 똑같음

                # 2-1-2. 홀수에 위치 & 극이 다름 => 방향 다름
                elif (n - (i+1)) % 2 != 0:
                    gear[i+1].rotate(direct * -1)
            elif r[i][1] == r[i+1][0]:  # 극이 같음(나만 회전)
                break  # 탈출 후 따로 돌려줄거임

    #지금까지 주변 톱니바퀴만 회전,
    #=> 최종적으로 나만 회전 시켜주면 됨
    gear[n].rotate(direct)


#3. 출력
result = 0
if gear[0][0] == 1:
    result += 1
if gear[1][0] == 1:
    result += 2
if gear[2][0] == 1:
    result += 4
if gear[3][0] == 1:
    result += 8

print(result)