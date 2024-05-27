'''
[트리] 트리 (골4)

-그래프에 트리가 없다면, "No trees.
-한 개라면, "There is one tree.
- (T > 1)라면 "A forest of T trees."

goal: 그래프가 주어질 때  트리의 개수를 세라.
'''

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def bfs(start):
    isCycle = False
    q = deque([start])

    while q:
        cnt_node = q.popleft()

        if visited[cnt_node]:
            isCycle = True
        visited[cnt_node] = 1

        for x in graph[cnt_node]:
            if visited[x] == 0:
                q.append(x)

    return isCycle



#정점, 간선
n,m = map(int,input().split())
case = 1

while n != 0 or m != 0:
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    cnt = 0

    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    #가능한 모든 연결요소를 순회
    for node in range(1, n+1):
        if visited[node] == 0:
            if not bfs(node):
                cnt += 1

    if cnt == 0:
        print(f'Case {case}: No trees.')
    elif cnt == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {cnt} trees.')

    case += 1
    n,m = map(int,input().split())