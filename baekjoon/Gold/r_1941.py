'''
[백트래킹] 소문난 칠공주 (골3)
형태 5*5

<규칙>
1. 7명으로 구성
ㄴ>이때 이들은 가로나 세로로 반드시 인접
3. 이다솜이던 임도연이던 상과 ㄴ
ㄴ> but 이다솜(S)파가 4명 이상은 되어야...4,5,6

goal: 7공주가 나올 수 있는 경우의 수
'''

from collections import deque

graph = [list(map(str, input().rstrip())) for _ in range(5)]
arr = [] #자리 조합 저장할 배열
result = 0 #최종 경우의 수



# 1. 7개의 조합이 서로 인접하는지 확인
def bfs(arr):
    # 이동할 방향 [상,하,좌,우]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    checked = [[True] * 5 for _ in range(5)]  # 방문 체크

    #7명의 여학생 위치를 0으로 초기화
    for i in arr:
        checked[i[0]][i[1]] = 0

    que = deque([(arr[0])]) #첫번째 여학생 위치는 큐에 집어넣음
    checked[arr[0][0]][arr[0][1]] = 1 #첫번째 여학생 방문처리함
    visited = 1 #여학생 위치 방문한 횟수

    while que:
        x,y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or nx >= 5 or ny < 0 or ny >=5:
                continue

            if not checked[nx][ny]:
                checked[nx][ny] = 1
                visited +=1
                que.append((nx,ny))

    if visited != 7: #7번 방문하지 않았다?
        return False
    else:
        return True



def dfs(depth, start, cnt):
    global result

    #임도연파가 4명이 넘는다 => 칠공주 (x)
    if cnt >= 4:
        return

    #7명 뽑힘
    if depth == 7:
        # 동시에 모든 여학생들이 전원이 붙어 있다(인접)
        if bfs(arr):
            result += 1
        return

    for i in range(start, 25):
        # 전체 25번 중 행 = i // 5
        x = i // 5
        y = i % 5

        #해당 위치 추가
        arr.append((x,y))
        #재귀함수 실행
        dfs(depth+1 , i+1, cnt + (graph[x][y] == 'Y'))
        arr.pop() #해당 위치 삭제



dfs(0,0,0)
print(result)

# import sys
#
# input = sys.stdin.readline
#
# graph = [list(map(str, input().rstrip())) for _ in range(5)]
# check = [[False] * 5 for _ in range(5)]
# s_cnt = 0
# result = 0
# # print(check)
#
# '''
# 1. 7공주로 영입하나?
#     1-1. 다 조회를하고 인접해도, 최종적으로 S>=4 여야함
#
# '''
# from collections import deque
# import copy
#
#
# def bfs(x, y ,visited):
#     global s_cnt, result
#     que = deque()
#     que.append((x, y, 1))
#
#     while que:
#         # print("현재 s_cnt",s_cnt)
#         x, y, depth = que.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             # 2. 범위를 벗어나면 종료
#             if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
#                 continue
#
#             if visited[nx][ny] : #방문 전적이 있다
#                 continue
#
#             # 종료 조건(7명 충족)
#             if depth == 7:
#                 print(nx,ny)
#                 if s_cnt < 4:
#                     continue
#                 else:
#                     print("result 값 = ", result,s_cnt)
#                     result += 1
#                     print(graph)
#
#
#         if graph[nx][ny] == 'S' or graph[nx][ny] == 'Y' :
#             if graph[nx][ny] == 'S':
#                 s_cnt += 1
#             # 방문체크
#             visited[nx][ny] = True
#             # print(visited)
#             # depth = 현재 7공주 사람
#             que.append((nx, ny, depth+1))
#
#
# # 이동할 방향 [상,하,좌,우]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# for i in range(5):
#     for j in range(5):
#         s_cnt = 0
#         visited = copy.deepcopy(check)
#         visited[i][j] = True  # 방문 시작
#
#         # bfs 실행
#         if graph[i][j] == 'S':
#             bfs(i, j, visited)
#
# print(result)
