#[dfs,bfs] 촌수계산 (실2)

n = int(input()) #전체 사람 수
a, b =map(int,input().split()) #촌수를 계산해줄 두 사람 번호
m = int(input()) #부모자식 관계 수

graph =[[] for _ in range(n + 1)]
visited = [0] * (n+1)

# 1 [2,3]
# 2 [1,7,8,9]
# 3 [1]    1 -3,2  2- 7
# 4 [5,6]
# 5 [4]
# 6 [4]
# 7 [2] 8 [2] 9[2]

#1. graph 관계 삽입 (부모 -자식)
for i in range(m):
    x,y = map(int, input().split()) #부모, 자식
    graph[x].append(y)
    graph[y].append(x)


#dfs로 풀어야 하지 않을까?
# 1. 타고 연결되어 있는 노드가 끊길 떄까지 확인해줘야 함
# 2. 더이상 접점이 없으면 -1 출력해야 해서s

cnt = 0
result = [] #결과 저장 값

def dfs(start,cnt):
    visited[start] = True #방문처리
    cnt+=1

    if start == b:
        result.append(cnt)

    # 해당 그래프 노드들 순차적 깊이탐색
    for v in (graph[start]):
        #방문한 적 있는가?
        if visited[v] == 0:
            #? 왜 cnt를 넣어주는가?
            dfs(v, cnt)

dfs(a,cnt)
# print(result)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)
