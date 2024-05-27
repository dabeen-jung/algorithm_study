'''
[트리] 트리의 부모찾기 (실2)


goal: 2번 노드부터 n까지 각 노드의 부모 구하기
'''
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)

def bfs(start):
    q = deque([start])
    # visited[start] = 0 #1번 노드엔 아무것도?

    while q:
        x = q.popleft()
        for v in graph[x]:
            if visited[v] == 0:
                #자신의 바로 위 부모노드 넣어주기
                visited[v] = x
                q.append(v)

bfs(1)
for i in range(2,n+1):
    print(visited[i])