#[스택] 탑 (골드5)
#rule
# 1. 신호는 가장 가까운 주변 중 자신보다 높은탑만 ok
# 2. 왼쪽 방향으로 신호를 보냄

#goal: 각각의 탑들이 순서대로 레이저를 발사시, 각 탑들의 수신한 레이저의 '도달 위치' 출력

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split())) #6 9 5 7 4
stack = []
res = [0] * n  # [0 0 2 2 4

for idx, tower in enumerate(arr): #  7
    # 현재 탑이 더 크기 때문에 레이저가 여기까지 오지 x
    # 그러니 현 탑보다 작은 애들은 stack에서 다 정리해줌
    while stack and stack[-1][1] <=tower:
        stack.pop()

    if stack:
        res[idx] = stack[-1][0] #탑 높이 # [ 2]

    stack.append((idx+1, tower)) [ 7 ]

print(' '.join(map(str,res)))