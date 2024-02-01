#[재귀] 별찍기(11) (골4)
# 규칙 유추
#goal : n 번째 줄까지 별 출력
# N은 3,6(하단에 2개),9(3개),12 층 ...형태로 3개 묶음이 반복

'''
  *
 * *
*****     -> N= 3 (3층임)
'''

import sys
input = sys.stdin.readline
N = int(input())
star = [[' ' for _ in range(N*2)] for _ in range(N)]
print(star)

def rep(x, y, k):
    if k <= 3: # 한 단위에서 세로 길이가 3이다
        for i in range(3):
            for j in range(i+1):
                star[x+i][y+j] = star[x+i][y-j] = '*'
        star[x+1][y] = ' '
        return

    size = k//2
    rep(x, y, size)
    rep(x+size, y-size, size)
    rep(x+size, y+size, size)

rep(0,N-1, N)

for i in range(N):
    print("".join(star[i]))
