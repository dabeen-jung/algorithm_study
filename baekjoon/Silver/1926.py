#[dfs,bfs] 그림 (실버1)
#goal : 그림의 개수, 그림의 가장 큰 넓이(dfs)
# 문제 발생 : 최대재귀 깊이
# 재귀함수 내부에서 자기자신을 너무 호출하면 -> 스택오버플로우 발생 -> 이를 방지하기 위해 제한함
# 보통은 1000으로 제한

import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

# visited =[]

def dfs(x,y):
    global max #한 그림에서 넓이측정
    global res #가장 큰 넓이
    global n_x,n_y
    #그림의 범위를 벗어날 경우 해당 dfs 탈출
    if x < 0 or x >= n or y < 0 or y >= m:
    # n,m을 포함해서 큰 경우 false임(0부터 시작하니까)
        return False

    if graph[x][y] == 1: #현 노드에 아직 방문 x함
        #맨 처음 돌릴 때 기록해두기
        if max == 0:
            n_x,n_y = x,y

        #방문이 안된 노드일 때마다 max증가(넓이)
        max += 1
        # 해당 노드 방문처리
        graph[x][y] = 0

        #상하좌우 재귀함수 시작
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        #dfs 그림이 완성되서 문을 닫는 마지막
        if x==n_x and y == n_y:
            if max > res:
                res = max
            max = 0
            return True
    return False


cnt = 0
max = 0
res = 0
n_x,n_y = 0,0
for i in range(n):
    for j in range(m):
        #현재 위치에서 dfs 실행
        if dfs(i,j) == True:
            n_x,n_y = i,j
            cnt+=1 #그림 갯수 증가

print(cnt,res,sep='\n')