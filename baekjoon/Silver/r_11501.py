'''
[그리디] 주식 (실2)
이익 += 팔가격 - 당시 산 가격

i) 팔자.
가격이 젤 비쌀 때
ii) 사자
가격이 젤 쌈
*Goal
일 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산
'''

import sys
input = sys.stdin.readline
t_c = int(input())

def f(arr):
    MAX = 0
    profit = 0

    for price in reversed(arr):
        if price > MAX:
            MAX = price
        else:
            profit += (MAX - price)
    return profit


for i in range(t_c):
    n = int(input())
    arr = list(map(int,input().rstrip().split()))
    print(f(arr))

