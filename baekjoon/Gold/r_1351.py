'''
[해쉬] 무한수열 (골5)
⌊x⌋ -7.8 => -8이다 ( 8.5 =>8

메모이제이션 + top-down식
'''

import sys
input = sys.stdin.readline

#모든 경우의 수를 구하는 bottom-up (x)
# 필요한 경우만 구하는 top-down 으로 구함
def f(k):
    i,j = k // P, k//Q

    if k in dp:
        return dp[k]
    else:
        dp[k] = f(i) + f(j)
        return dp[k]


N,P,Q = map(int, input().split())
dp = {}
dp[0] = 1


print(f(N))