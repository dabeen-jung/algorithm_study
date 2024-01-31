# [백트래킹] n과 m(3) (실3)
# 같은 수를 여러번 고르는게 가능함

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
result = []

def f(dept):
    if dept == m:
        print(' '.join(map(str, result)))
        return

    for i in range(1,n+1):
        result.append(i)
        f(dept+1)
        result.pop()

f(0)