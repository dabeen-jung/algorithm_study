'''
[시뮬레이션] 스타트와 링크 (실1)
* 팀 능력치 = 모든쌍의 능력치들의 합
ex) Sij와 Sji는 다름 => i,j가 팀에 들어가면 Sij + Sji 이다

* 조합 구하는법
1. for문으로 하나씩
for i, j in combinations(team, 2):
    #(i,j) //(1,2) 이렇게 1개씩 나옴
혹은
2. list 묶음으로 한 번에
조합 = list(combinations(team, 2))
//하면 [(1, 2), (1, 3), (2, 3)] 나옴

goal: 각 팀의 능력치 조합에서 차이가 가장 적은(최솟값)을 찾아서 출력해라
'''

import sys
input  = sys.stdin.readline
from itertools import combinations

N = int(input())
S = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [0]*(N+1)
visited[0] = -1
MIN = float('inf')

# 합만 구하는 함수
def team_score(team):
    #1. 이 인덱스의 모음에서 나올 수 있는 조합의 합을 구함
    score = 0
    #[(1, 2), (1, 3), (2, 3)] => (1, 2) 하나씩 나옴
    for i, j in combinations(team, 2):
        # print(i+1,j+1)
        score += S[i][j] + S[j][i]  # ij + ji
    # print("score" ,score)
    return score





def f(depth, num):
    global MIN

    if depth == (N//2):
        #visited 배열을 넘겨 스타크 팀, 링크팀별 합을 구하고, 비교까지
        stark = [i-1 for i, x in enumerate(visited) if x == 1]
        link = [i-1 for i, x in enumerate(visited) if x == 0]

        # 차이를 비교했을 때 최솟값이여야 함
        diff = abs(team_score(stark) - team_score(link))
        MIN = min(diff, MIN)
        return

    for i in range(num,N+1):
        if depth == 0 and i == 2: #이 이상 만들 필요가 없다.
            break
        if visited[i] == 0:
            visited[i] = 1
            f(depth + 1, i+1)
            visited[i] = 0 #반환

# 첫시작은 num=1부터, 그래야 1번부터 계산함
f(0,1)
print(MIN)