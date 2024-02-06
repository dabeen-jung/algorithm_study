'''
#[백트래킹] 부분수열의 합 (실2)

1. 중복 x, 12 21(x)
반례 5 0
0 0 0 0 0 =>31

'''

import sys
input = sys.stdin.readline

n,s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
# result = []

def f(idx, sum):
    global cnt

    if idx != 0 and sum == s:
        # print(",",start)
        cnt +=1 #누적됨
        # return이 없는 이유: 뒤에 똑같은 값이 또 올 수도 있으니 다 돌고
        #for문 종료 후 다음께 도는거 맞다

    for i in range(idx,n):
        sum += arr[i]
        #result.append()
        f(i+1, sum)
        #reuslt.pop()
        # ㄴ>(문제) 뒤에 정답인 수와 같은 경우의 수가 있었을 때 안 세고 나가버림
        sum -= arr[i]

f(0,0)
print(cnt)