'''
2일차 - sum


goal: '각 행의 합', '각 열의 합', '각 대각선의 합' 중 최댓값을 구하는
'''

for tc in range(1, 11):
    t = int(input())
    MAX = 0
    col = [0]*100
    left,right = 0,0

    for i in range(100):
        #각 행별로 입력
        row = list(map(int,input().split()))
        #대각선 합 구하기
        left += row[i]
        right += row[100 - (i+1)]

        for j in range(100):
            col[j] += row[j] #각 컬럼을 행별로 누적

        #1. 행의 최대합 구하기
        MAX = max(MAX, sum(row))
    #2,3. 대각선들과 열들, 행 중 최대합 구하기
    MAX = max(MAX, left, right, max(col))

    #각 대각선까지 모아서 최대를 구함
    print('#%d %d'%(t, MAX))