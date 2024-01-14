# [bfs] 숨바꼭질 (실1)
# 이동: 앞뒤,2*현재위치
#goal: 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인가
# 최대한 적게 돌아서 최단거리로 구해야함

#bfs 선정 이유: 시작 노드에서 가까운 노드부터 차례대로 방문
#dfs는 보통 1. 경로 자체 탐색, 2. 모든 노드를 탐색 해야할 때


from collections import deque

def bfs(N, K):
    MAX_SIZE = 100000
    queue = deque([N])
    visited = [0] * (MAX_SIZE + 1)

    while queue:
        x = queue.popleft()

        if x == K:
            return visited[x]

        for nx in [x-1, x+1, x*2]:
            if 0 <= nx <= MAX_SIZE and visited[nx] == 0:
                # 이동시간 = 이미 계산 했던 것에 + 경우의 수(1,2,3 중 하나)
                # => x번 계산에 1번 더 계산함(누적해줘야함)
                # 17을 계산해서 오려면 그 전의 수는 => 18,16, 2*?=17일 수 없음(x)
                visited[nx] = visited[x] + 1
                queue.append(nx)

N, K = map(int, input().split())
print(bfs(N, K))

