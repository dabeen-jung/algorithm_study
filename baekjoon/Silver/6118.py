'''
[그래프] 숨바꼭질 (실1)

-헛간은 1번부터 찾을거다.
- 헛간은 m개의 양방향 길을 가짐 ( 끝은 ai,bi)
- 어떤 헛간 -> 다른 헛간으로 이동 가능

goal : 즉 1번에서 최대한 먼 헛간(노드)과, 거기까지의 거리
-> '냄새'는 1번 헛간에서의 거리가 멀어질수록 감소한다고 한다.
(여기서 거리라 함은 지나야 하는 길의 최소 개수이다)
'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    # 여기서  누적된 것을 반환함
    visited[start] = 0
    q = deque([start])

    while q:
        x = q.popleft()

        for next in graph[x]:
            if visited[next] == -1: #방문 x
                #깊이 계산
                visited[next] = visited[x] + 1
                q.append(next)
    return visited

#1.입력값
n,m = map(int,input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

res = bfs(1)

distance = max(res) #헛간까지의 거리
cnt = 0 #같은 거리를 갖는 헛간 갯수
MIN = float('inf')
for i in range(1,n+1):
    if distance == res[i]:
        if i < MIN:
            MIN = i
        cnt += 1

print(MIN, distance, cnt )