'''
[백트래킹] N과 M(4) 
rule:
1. 중복 x
2. 중복이 되지 않는 선에서 사용 가능 112(0), 121(x)

'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
result = []


def rep(start, depth):
    if depth == m:
        print(' '.join(map(str,result)))
        return
    #당장 앞의 수와 같으면 된다.
    for i in range(start,n+1):
        result.append(i)
        rep(i, depth+1)
        result.pop()

rep(1,0)
