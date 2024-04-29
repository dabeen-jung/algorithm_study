'''
[] 멀티버스2 (골5)
M개의 우주, - 1~N까지 행성 존재
균등  = A우주 행성 - B우주 행성끼리 조건을 하나라도 만족함 => 행성 구성의 순위가 동일함
ex) 1 3 2, B: 1 3 2 동일
goal: 균등한 우주의 쌍의 갯수 (행성이 x)
'''

import sys

input = sys.stdin.readline
from collections import defaultdict

#우주 갯수, 행성 갯수(우주 내)
m, n = map(int, input().split())
universe = defaultdict(int)

for _ in range(m):
    # 행성 입력 받기
    planets = list(map(int, input().split()))

    # 행성 정렬 ( 구성 같은 행성 한개만 세기 )
    sortedPlanets = sorted(list(set(planets)))

    # 행성 순위 지정
    rank = {sortedPlanets[i]: i for i in range(len(sortedPlanets))}
    # print(rank)

    # 입력 받은 행성에 맞게 '순위 저장' (0, 2, 1)
    vector = tuple([rank[i] for i in planets])
    # print(vector)
    # 해당 순위 벡터에 대한 개수 추가
    universe[vector] += 1
    # print(universe)

sum = 0

for i in universe.values():
    # print(i)
    # n개 중 2개의 우주를 엮어야 하기 때문에 n C 2 를 해줘야 함 (중복 제외)
    sum += (i * (i - 1)) // 2  # nC2

print(sum)