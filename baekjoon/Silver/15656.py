#[백트래킹 ] n과 m(7) (실3)

import sys

n,m = map(int,input().split())
arr = list(map(int, input().split()))
result = []
arr.sort()

def rep(depth):
    #종료조건
    if depth == m:
        print(' '.join(map(str,result)))
        return

    for i in range(n):
        result.append(arr[i])
        rep(depth+1)
        result.pop()

rep(0)
