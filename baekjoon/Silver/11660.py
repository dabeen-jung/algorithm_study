# 구간 합 구하기 5(실버1)

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
matrix = [[0]*(n+1) for _ in range(n+1)]

# print(matrix)

for i in range(1,n+1):
    for j in range(1,n+1):
        # 밑으로 한 번 간 행+ 옆으로 간 열 -누적합(직전) + 공백으로 인해 arr더해주기
        matrix[i][j] = matrix[i][j-1] + matrix[i-1][j] -matrix[i-1][j-1] \
                       + arr[i-1][j-1]

# print(matrix)

for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    #x1등과 같이 인덱스가 1부터 시작하더라도 그냥 대입가능함 위에서
    #우리는 [0]을 1행 더 추가했고 1열 더 추가 했기 때문
    # 직전 누적합을 빼줘야 함
    cnt = matrix[x2][y2] - matrix[x2][y1-1] \
          - matrix[x1-1][y2] + matrix[x1-1][y1-1]

    print(cnt)

# 행만 생각하고 짜서 오답
#matrix = [[0] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         matrix[i].append(matrix[i][-1]+arr[i][j])
#
# # print(matrix)
#
#
# for i in range(m):
#     x1,y1,x2,y2 = map(int,input().split())
#     cnt = 0
#     for j in range(x1-1,x2):
#         cnt += (matrix[x1-1][y2]-matrix[j][y1-1])
#     print(cnt)
