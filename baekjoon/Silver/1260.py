# [dfs, bfs]  DFS와 BFS (실버2)
#goal: DFS , BFS 각각의 탐색 결과를 출력
# 조건: 번호가 작은 순대로 방문
from collections import deque


def bfs(graph, visited,start):
    que = deque([start])
    visited[start] = True

    while que:
        val = que.popleft()
        print(val, end=' ')

        #인접노드,방문전적 x
        for i in graph[val]:
            if visited[i] == False:
                que.append(i)
                visited[i] = True



def dfs(graph, visited, start):
    # 현재 방문처리
    visited[start] = True
    print(start, end=' ')

    #인접한 노드 하나씩 꺼냄, 방문x 노드 탐색 시작
    for i in graph[start]:
        if visited[i] == False:
            dfs(graph, visited, i)



n,m,v = map(int,input().split())
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
graph = [[] for _ in range(n+1)]



dfs_res = []
for i in range(m):#배열에 노드 마다 연결 노드 재정리
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

for i in graph:
    i.sort()

dfs(graph, visited_dfs, v)
print()
bfs(graph, visited_bfs, v)


