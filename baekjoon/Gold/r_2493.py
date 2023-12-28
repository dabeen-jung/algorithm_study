#[스택] 탑 (골드5)
#rule
# 1. 신호는 가장 가까운 주변 중 자신보다 높은탑만 ok
# 2. 왼쪽 방향으로 신호를 보냄

#goal: 각각의 탑들이 순서대로 레이저를 발사시, 각 탑들의 수신한 레이저의 '도달 위치' 출력

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

stack = []
res = [0] * n

for idx, tower in enumerate(arr):
    # 현 탑의 높이가 앞의 탑보다 훨씬 높으면
    while stack and stack[-1][1] <=tower:
        stack.pop()

    if stack:
        res[idx] = stack[-1][0] #탑 높이

    stack.append((idx+1, tower))

print(' '.join(map(str,res)))