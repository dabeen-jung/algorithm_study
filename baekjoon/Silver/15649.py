# [백트래킹] N,M

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
result = []
check = [False] * (n+1)

def rep(num):
    if num == m:
        print(' '.join(map(str, result)))
        return

    for i in range(1, n+1):
        if check[i] == False:
            check[i] = 1
            result.append(i)
            rep(num+1)
            #함수 다녀와서 check,result 배열 다시 초기화해줌
            check[i] = False
            result.pop()

rep(0)

