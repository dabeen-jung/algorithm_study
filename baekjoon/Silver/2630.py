#[재귀] 색종이 만들기 (씰2)

import sys
input = sys.stdin.readline


n = int(input())
paper = [list(map(int, input().rstrip().split())) for _ in range(n)]

blue, white = 0,0

def rep(s_row, s_col, divid):
    global blue,white

    #맨 첫번째 칸 값
    num = paper[s_row][s_col]
    flag = 0

    for i in range(s_row, s_row + divid):
        for j in range(s_col, s_col + divid):
            if paper[i][j] != num:
                flag = 1
                break
        if flag:
            break


    # 현재 종이가 전부 같은 수
    if not flag:
        if num:
            blue += 1
        else:
            white += 1

    else: #같은 색들이 아님

        divid //= 2 # 2로 나눠줌

        rep(s_row, s_col, divid)
        rep(s_row, s_col + divid, divid)

        rep(s_row + divid, s_col, divid)
        rep(s_row + divid, s_col+divid, divid)


rep(0,0,n)
print(white)
print(blue)
