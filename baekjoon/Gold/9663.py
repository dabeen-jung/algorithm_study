'''
[백트래킹] N-Queen (골4)
참고 https://seongonion.tistory.com/103
* goal:
1. 퀸끼리 '서로 공격할 수 없게' 놓는 '경우의 수'

* 퀸 특징
1. 수평 이동: 같은 행 어디던 (이동 가능)
2. 수직 이동: 같은 열 어디던 (이동 가능)
3. 대각선 이동
4. 공격:
    퀸이 이동하는 경로에서 '마주친 첫 번째 '상대 말'을 공격'
    - 다른 말을 뛰어 넘거나 / 자신의 말을 공격 할 수 x
5.
'''

import sys
input = sys.stdin.readline

N = int(input())
graph = [0] * N
cnt = 0 #경우의 수


#2. 퀸들끼리 서로 공격하는지 여부 확인
def is_attack(row):
    for i in range(row):
        #if 이곳에서의 행에 대한 열이 겹치는 경우거나 (공격받음)
        if graph[row] == graph[i] \
                or abs(graph[row] - graph[i]) == abs(row-i):  #or 대각선 관계(공격받음)인가
            return False # 공격함
    return True #공격받지 않음 =>cnt+=1


# 1. 행에 퀸을 하나씩 배치
def queen(row):
    global cnt

    if row == N:
        cnt+=1
        return
    else:
        for i in range(N):
            # row = 행, i = 열
            # ex) 0행에 1열, 1행에 3열 => [1,3,...]
            graph[row] = i
            # 공격이 x면? => 다음 행의 퀸 배치(함수호출)
            if is_attack(row):
                queen(row+1)

queen(0)
print(cnt)