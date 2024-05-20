'''
[그래프] 케빈 베이컨의 6단계 법칙 (실1)

강호 - 세희
강호 - 민호 - 백준 - 선영 - 도현 - 세희 => 5단계

* 모든 사람은 친구 관계로 연결되어져 있다. (1-n까지 무조건 돌거임)

goal: 백준 유저수가 입력될 때, 케빈 베이컨 수가 가장 적은 사람 번호
 그런 사람이 여러 명일 경우에는 번호가 가장 작은 사람을 출력
(임의의 두 사람이 최소 '몇 단계 만에' 이어질 수 있는지 계산)
'''
from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    q = deque([start])
    visited[start] = 1
    num = [0] * (n+1) # i번째까지 거치는 노드들의 갯수가 적힘

    while q:
        x = q.popleft()
        for i in relations[x]: #해당 출발노드에서 꺼냄
            if visited[i] == 0:
                # visited[i] = visited[x] + 1
                # 이전 num[x]를 들린후 num[i]를 들리니까 +1만 해주면 됨
                num[i] = num[x] + 1
                visited[i] =1
                q.append(i)
    # print(num)
    return  sum(num)


#유저 수, 관계 수(친구)
n,m = map(int,input().split())
relations = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    relations[a].append(b)
    relations[b].append(a)

res = []

for i in range(1, n+1): #n번까지와의 관계
    visited = [0] * (n+1)
    res.append(bfs(i)) #결과 입력

#값이 가장 작은,동시에 index가 가장 작은
print(res.index(min(res))+1)