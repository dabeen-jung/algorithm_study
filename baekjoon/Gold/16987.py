'''
[백트래킹] 계란으로 계란치기 (골 5)
내구도, 무게

- 계란을 내리침 =  내구도 = 기존 내구도 - 상대무게
- 내구도 0 이하면, 깨짐

*주의
 1. 한 번만 치고 넘어감
 2. 제일 왼쪽 계란부터 시작해서 오른쪽으로 들어올림

* 내리치는 동작 (x) 경우
1. '들고 있는' 계란이 깨짐
=> * 들고 있는 계란 오른쪽을 듦

* 종료
- 맨 오른쪽 계란의 순서가 오면 종료
- 더이상 '깨트릴' 계란이 목록에 없음

goal: 최대 몇 개의 계란을 꺨 수 있는가? (차례대로 주어질때)
비교: 현재 누적된 cnt보다 더 많이 깨진 경우의 cnt가 나왔는가?
'''

import sys
input = sys.stdin.readline

N = int(input())
arr = []
cnt = 0
check = [False] * N

for i in range(N):
    s,w = map(int, input().rstrip().split())
    arr.append([s,w])


#(내구도, 무게)
def crush(nowIdx):
    global cnt

    #종료조건 1. 맨 오른쪽을 들어올림
    if nowIdx == N:
        realBreak = 0
        for i in range(N):
            if arr[i][0] <= 0: #깨졌는가
                realBreak += 1 #카운팅
        #둘 중 누가 더 많이 계란을 깨는 경우인가
        cnt = max(cnt, realBreak)
        return

    # if 2. 손에 들고 있는 계란이 깨짐 => 다음 계란을 든다 (종료 x)
    if arr[nowIdx][0] <= 0:
        # cnt+=1 나와서 카운트
        # cnt += 1
        crush(nowIdx + 1)
        return

    #elif 2) 나 빼고 계란이 다 깨져있는 경우 (종료)
    isAllBrk = True
    for idx in range(N):
        if idx == nowIdx:
            continue

        # 하나라도 안 깨진게 있었다.
        if arr[idx][0] > 0:
            isAllBrk = False
            break
    if isAllBrk: #다 깨진경우였다.
        # 자신을 빼고 깨진 계란 수,
        cnt = max(cnt, N-1)
        return


    # 들고 있는 계란으로 다른 계란을 때리는 모든 경우의 수
    # => 들고 있는 계란으로는 1번만 칠 수 있다.
    for i in range(N):
        #나 자신/ 조회한 계란이 이미 망가진걸 조회하면=> Pass
        if i == nowIdx or arr[i][0] <= 0:
            continue

        #계란 깨기 (내구도 감소)
        arr[i][0] -= arr[nowIdx][1] #2
        arr[nowIdx][0] -= arr[i][1] #1
        crush(nowIdx + 1) #함수 호출, -> 옆 계란을 듦

        #복구
        arr[nowIdx][0] += arr[i][1]
        arr[i][0] += arr[nowIdx][1]


crush(0)
print(cnt)