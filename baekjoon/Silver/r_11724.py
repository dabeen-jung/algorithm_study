#[dfs,bfs] 연결 요수의 개수 (실)
#goal: 연결 요수의 개수를 구하라?
# 연결요소 : 연결된 노드끼리의 묶음
# 왜 바로 못풀었을까? 복잡하게 생각함.


import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited =[0] * (n+1)
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()



def dfs(start):
    global cnt
    visited[start] = 1

    for v in graph[start]:
        if visited[v] == 1:
            continue

        if visited[v] == 0: #방문처리 x
            dfs(v)

cnt = 0
for i in range(1,n+1):
    if visited[i] == 0:
        dfs(i)
        cnt+=1 #연결 끊기면 어차피 종료됨

print(cnt)