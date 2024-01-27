#[재귀] 종이의 개수 (실2)
#1. 종이에 숫자들이 모두다 같다 => 그대로 씀
#2. 1이 아니다, 같은 크기의 종이 9개로 잘라냄-> 1번으로

import sys
input = sys.stdin.readline


def rep(start_row, start_col, size):
    global zero_cnt, minus_cnt, one_cnt

    #첫번째 수
    num = arr[start_row][start_col]
    flag = 1

    for i in range(start_row, start_row + size):
        for j in range(start_col, start_col + size):
            if num != arr[i][j]: #첫번쨰 요소와 값이 틀림
                flag = 0
                # print("flag = ", flag)
                break
        #flag가 0이다-> 탈출
        if not flag:
            break


    if flag: # 현 종이의 숫자가 다 같다 => 종이 갯수 +1
        if num == -1:
            minus_cnt += 1
        elif num == 0:
            zero_cnt += 1
        else:
            one_cnt += 1

    else: #종이자르고 다시 반복
        size //= 3

        rep(start_row, start_col, size )
        rep(start_row, start_col + size, size)
        rep(start_row, start_col + (size*2), size)

        rep(start_row + size, start_col, size)
        rep(start_row + size, start_col + size, size)
        rep(start_row + size, start_col + (size * 2), size)

        rep(start_row + (size * 2), start_col, size)
        rep(start_row + (size * 2), start_col + size, size)
        rep(start_row + (size * 2), start_col + (size * 2), size)


# 1. 입력값 받기
n = int(input())
arr = [list(map(int,input().rstrip().split())) for _ in range(n)]

#갯수들
zero_cnt = 0
minus_cnt = 0
one_cnt = 0

# 함수 실행
rep(0,0,n)

print(minus_cnt)
print(zero_cnt)
print(one_cnt)