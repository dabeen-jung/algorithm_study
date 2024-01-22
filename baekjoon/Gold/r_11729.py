#[재귀] 하노이의 탑 이동순서 (골5)
# 첫번째에서 3번째 장대로 옮길 것인데 이동 순서 출력하고 이동횟수를 최소로 출력
#goal: 이동 홧수가 최소, 그 과정 출력

import sys
input = sys.stdin.readline



def rep(k, start, end):
    if k == 0:
        # print(start, end)
        return
    # 6-start-end하면 넘겨야 할 막대 위치가 나옴
    rep(k-1, start, 6-start-end) #1단계
    print(start,end) #2단계
    rep(k-1, 6-start-end, end) #3단계)

k = int(input())
print(2**k-1)
rep(k,1,3)