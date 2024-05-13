'''
[그래프] 결혼식 (실2)
상근이-친구-친구까지만 초대할 예정

goal: 결혼식에 초대하는 동기의 수

왜 틀렸는가? dfs 접근 실패 + dfs,bfs 이용 까먹음
'''
from collections import deque

def bfs(start):
    #초기 세팅
    q = deque()
    q.append((start,0)) #상근이가 시작

    visited = [0] * (n + 1)  # 방문처리 배열
    visited[start] = 1
    result = 0

    while q:
        # print("남은 큐들",q)
        #시작노드,depth
        x,cnt = q.popleft()

        for i in graph[x]:
            if visited[i] == 0 and cnt < 2:
                visited[i] = 1
                q.append((i,cnt+1)) #시작노드,depth+1
                result += 1
    return result

n = int(input()) #동기의 수(상근이 포함)
m = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


print(bfs(1))

#[dfs - 못품 - 틀렸다고 나옴]
# def dfs(start,cnt):
#     #친구의 친구까지만 가능 => 2
#     if cnt > 2:
#         return
#
#     for v in (graph[start]):
#         if visited[v] == 0: #방문을 하지 않음
#             visited[start] = 1
#         dfs(v, cnt+1)
#
# visited =[0] * (n+1)
# visited[1] = 1 #방문함
#
# dfs(1,0)
# #print(visited)
# # 방문(친구의 친구)한 노드들에서 - 상근이 제외
# print(len(list(filter(lambda x:x==True, visited))) - 1)

