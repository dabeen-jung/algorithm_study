#[dfs,bfs] 바이러스 (실버3)
#왜 틀렸을까? dfs 알고리즘 이해도 부족

# 2.함수 정의
# 왜 dfs인가? (bfs도 가능함)
# 어디까지 바이러스가 닿을 수 있을지 깊이를 봐야 하니까?
def dfs(start):
    global cnt # 함수 외부에 있어 함수가 끝나면 cnt 반영이 안되기 때문에 처리.
    # 현재 노드 방문처리
    visited[start] = True

    #현재 노드의 주변에 인접한 노드 재귀방문
    for i in graph[start]:
        if visited[i] == False:
            dfs(i)
            cnt+=1


# 1. 입력값 받기
n = int(input())
computer = int(input())

visited =[False] * (n+1) #방문여부
graph = [[] for _ in range(n+1)]
cnt = 0

for i in range(computer):
    a,b = map(int,input().split())
    #각 노드와 연결된 애들끼리 묶어줌
    graph[a].append(b)
    graph[b].append(a)


# 1과 연결된 컴퓨터들 다 거치기
dfs(1)
print(cnt)



