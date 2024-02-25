'''

[백트래킹] 차이를 최대로 (실2)

goal:  배열의 순서를 적절히 바꿔서 식의 최댓값을 구해라
식: |[0] - [1]| + |[1] - [2]|... + |[n-2] - [n-1]|

'''

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().rstrip().split()))
MAX = float('-inf')
arr=[]
visited = [0]*n

def f(depth):
    global MAX

    if depth == n:
        result = 0
        for i in range(n-1):
            result += abs(A[arr[i]] - A[arr[i+1]])
        MAX = max(result, MAX)
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(i)
            f(depth + 1)

            visited[i] = 0
            arr.pop()

f(0)
print(MAX)


# import sys
# from itertools import permutations
#
# n = int(sys.stdin.readline())
# graph = list(map(int,sys.stdin.readline().split()))
#
# max_ans = float('-inf')
#
# for i in permutations(graph):
#   ans = 0
#   for j in range(n-1):
#     ans += abs(i[j] - i[j+1])
#   max_ans = max(max_ans,ans)
#
# print(max_ans