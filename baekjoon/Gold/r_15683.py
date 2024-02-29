'''
[시뮬레이션] 감시 (골4)

0: 빈칸, 6: 벽, 1~5: CCTV(8개 이하), 감시할 수 있는 영역 : #

* 사각지대 : CCTV가 감시 못하는 영역
* CCTV 특징 : 1. 회전은 90도 방향만, 2. 벽(6)은 통과 x

goal: 사각지대의 최소크기 (즉, 최대한 많은 감시(#)를 해야함)
목표 1. #의 갯수가 제일 많은 것을 기억해야함

<왜 못했는가?>
- 모든 cctv 방향을 고려해 dx,dy를 짜고 이를 백트래킹에 적용해야 겠다 생각했지만,
구현하지 못함 (dx,dy에서)
- 회전을 고려하지 못함

'''

import copy
import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
graph = []
cctv = [] #cctv번호, x,y좌표
MIN = float('inf')

#남,동,북,서 를 가리킴(90도 반시계 방향으로)
dx = [-1,0,1,0]
dy = [0,-1,0,1]

direct = [ #cctv 번호 별 '방향 정보'
     [],
     [[0],[1],[2],[3]], #1번 cctv - 방향 4가지 (남동북서)
     [[0,2], [1,3]], #2번 cctv - 2가지 (남북,동서)
     [[0,1],[1,2],[2,3],[3,0]], # 3번 cctv - 4가지
     [[0,1,2],[1,2,3],[2,3,0],[3,0,1]], # 4번 cctv - (남동북,동북서,북서남,서남동)
     [[0,1,2,3]] # 5번 cctv - 1가지 (남동북서)
]

# 1. 입력값 및 cctv 좌표정보 받기
for i in range(n):
    #1행씩
    data = list(map(int,input().rstrip().split()))
    graph.append(data)
    for j in range(m):
        if data[j] in [1,2,3,4,5]: #이 값이 cctv인가?
            cctv.append([data[j], i, j])


# 2. 감시(탐색) 시작
def survelid(graph, d, x, y):
    for i in d: #cctv 방향 따라 1개씩 탐지
        nx = x
        ny = y
        while True:
            nx = nx + dx[i]
            ny = ny + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            if graph[nx][ny] == 6: #벽 만나서 종료
                break
            #감시 가능
            elif graph[nx][ny] == 0:
                graph[nx][ny] = -1


# 3. dfs함수
def dfs(depth , graph):
    global MIN
    if depth == len(cctv): #cctv 좌표 다 탐색
        cnt = 0
        for i in range(n):
            # 0=빈방 갯수 찾기(사각지대)
            cnt += graph[i].count(0)
        MIN = min(cnt, MIN)
        return

    # 감시를 하고 온 graph를 복사하여 이것으로 진행
    graph_copy = copy.deepcopy(graph)
    # print("진행", graph_copy)
    cctv_num, x, y = cctv[depth] #탐색할 cctv
    # print("cctvnum은)",cctv_num)

    #[[0,2], [1,3]]
    for d in direct[cctv_num]: #n번 cctv가 돌 수 있는 방향을 가져옴
        survelid(graph_copy,d, x, y ) #감시시작
        dfs(depth + 1, graph_copy) #다음 감시

        #return 된 후
        #graph_copy : dfs의 종료조건 후 return된 상태
        graph_copy = copy.deepcopy(graph)


dfs(0, graph)
print(MIN)