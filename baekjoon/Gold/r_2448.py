#[재귀] 별찍기(11) (골4)
# 규칙 유추
#goal : n 번째 줄까지 별 출력
# N은 3,6(하단에 2개),12 층 ...형태로 3개 묶음이 반복

'''
  *
 * *
*****  (5)   -> N= 3 (3층임)
'''

import sys
input = sys.stdin.readline
N = int(input())

# N*2 => 가장 밑 행의 열*2 => ' ' 만듦
# 가운데 빈공간 때문에 *2임
star = [['_' for _ in range(N*2)] for _ in range(N)]
# print(star)

# rep(0,5,6)  -> N=6
#x = 행, y= 이 묶음에서의 중심 위치, size = 3묶음인지 여부 확인
def rep(x, y, k):
    #(0,5,3)
    if k <= 3: # 한 단위에서 세로 길이가 3이다 (k는 0~3까지만)
        for i in range(3):
            for j in range(i+1): # 0, 0~1, 0~2,
                # 열이 *_* 처럼 양쪽으로 *이 만들어짐   *****
                # 각 행에서 대칭하는 열들을 표시
                #star(0+0)[5+0] = star[0+0][5-0] => star[0][5]=star[0][5] ='*'
                star[x+i][y+j] = star[x+i][y-j] = 'A'
                print('x= %d, y= %d,i=%d, j = %d'%(x,y,i, j))
                print(star)
        star[x+1][y] = ' ' # 해당 묶음의 1행 중 가운데를 비워줌 (y=n-1)
        return

    #size= 6//2=>3
    size = k//2     #size의 뜻: 한 묶음이 되는지 여부
    rep(x, y, size)     #위에 묶음
    rep(x+size, y-size, size)   #왼쪽 밑에 묶음
    rep(x+size, y+size, size)   #오른쪽 밑에 묶음

rep(0,N-1, N)

for i in range(N):
    print("".join(star[i]))
