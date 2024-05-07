'''
[dfs,bfs] 그림
goal: 그림 중 넓이가 가장 넓은 것의 넓이를 출력

그림의 기준 : 1이 가로세로로 붙어 있는거
'''

import sys

sys.setrecursionlimit(10000000)

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

# 이 방향벡터 사용해서 for문 돌리면 메모리 초과
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

areas = []
cnt = 0


def dfs(x, y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0

        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

# 방향벡터로 for문 돌리면 메모리 초과
#   for i in range(4):
#      nx = x+dx[i]
#      ny = y+dy[i]
#      dfs(nx,ny)

        return True
    return False

for i in range(n):
    for j in range(m):
        # 1일때만
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            areas.append(cnt)

if len(areas) == 0:
    print(0, 0, sep='\n')
else:
    print(len(areas))
    print(max(areas))