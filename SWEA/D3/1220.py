'''
5일차 - Magnetic

푸른 S(2)< -> N(1)붉은

* 교착 상태 1/2여야 함
갯수가 많더라도, 반대 방향으로 움직이는 자성체가 하나라도 있다? ->움직이지 않는다.
=> 누르는 조합이 붉,푸의 형태일 경우? 각 1개씩
goal : 자성체들이 서로 충돌하여 남게된 '교착상태' 갯수
'''

for tc in range(1,11):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    #열 기준으로 봐야함
    cnt = 0
    for j in range(n): #열 탐색
        row = 0
        stack = []

        while row < n: #1개의 행을 다 돌 때까지
            # 스택에 1.이후 2가 쌓이면=> 교착 발생임
            if not stack and arr[row][j] == 1: #스택이 비여있는데 1이 오면.=>수용
                stack.append(1)
            elif stack and stack[-1]==1 and arr[row][j] == 2: #스택 마지막이 1이고 그 위로 2가 ㅇ면
                stack.pop()
                cnt += 1
            row += 1

    print(f'#{tc} {cnt}')