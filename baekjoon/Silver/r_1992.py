#[재귀] 쿼드트리 (실1)
# 포인트 : 0 or 1만 가지는 정사각형 범위를 구한다(4등분을 계속해서)

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().rstrip())) for _ in range(n)]
# print(arr)
# answer = ''

def f(s_row, s_col, size):
    # (값이 하나만 남음)=> 나눌 것도 없음
    if size == 1:
        print(arr[s_row][s_col], end = '')
        return
    num = arr[s_row][s_col]

    for i in range(s_row, s_row + size): #시작~ 시작+size
        for j in range(s_col, s_col + size):

            # 탐색 시작 -> 탐색 결과는 (_)에 담아줌
            if num != arr[i][j]:
                print("(", end = "")
                size //= 2

                # Z방향으로 돎
                f(s_row, s_col, size) #1사분면
                f(s_row, s_col + size , size) #2사분면
                f(s_row + size, s_col, size) #3사분면
                f(s_row+size, s_col+size, size) #4사분면
                print(")", end = '') #탐색 종료
                return

    print(arr[s_row][s_col], end='')
    return

f(0, 0, n)
# print(answer)
