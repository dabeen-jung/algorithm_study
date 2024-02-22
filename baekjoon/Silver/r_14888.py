'''
[백트래킹] 연산자 끼워넣기 (실1)

1. 수는 순서를 못바꿈
2. 연산은 무조건 순서대로(우선순위 x)
3. -6 // 3 => 6//3 => 2*-1 = -2 여야함 (몫만 취함)

* goal
1. 식의 결과 최대/ 최소를 출력
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))
# +, -, *, //
add, sub, mul, div = map(int, input().rstrip().split())

MIN = float('inf')
MAX = float('-inf')


def dfs(depth,num):
    global MIN,MAX
    global add, sub, mul,div

    if depth == n:
        MAX = max(MAX, num)
        # print("max = ", MAX)
        MIN = min(MIN, num)
        return

    # 1. 배열의 수들을 늘여놓음

    if add > 0:
        add -= 1
        # print("add", depth, num + arr[depth])
        dfs(depth + 1, num + arr[depth])
        add += 1  # 복귀

    if sub > 0:
        sub -= 1
        # print("sub", depth, num - arr[depth])
        dfs(depth + 1, num - arr[depth])
        sub += 1


    if mul > 0:
        mul -= 1
        # print("mul", depth, num * arr[depth])
        dfs(depth + 1, num * arr[depth])
        mul += 1

    if div > 0:
        div -= 1
        # print("div", depth, num // arr[depth])
        dfs(depth + 1, int(num / arr[depth]))
        div += 1

#함수 호출
dfs(1,arr[0])

print(MAX)
print(MIN)