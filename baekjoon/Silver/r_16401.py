'''
[DP] 과자 나눠주기

goal: 최대한 긴 과자를 주자 (같은 길이)
'''

#m 조카의 수
m,n = map(int, input().split())
L = list(map(int, input().split()))

start = 1 #과자길이는 최소 1부터
end = max(L)
result = 0

while start <= end:
    mid = (start + end) // 2 #중간값

    cnt = 0 #조카 몇명이 받을 수 있는가
    for i in L:
        cnt += i // mid
    # 막대가 조카들 수보다 많다 -> (길이를 더 늘릴 수 있다)
    if cnt >= m:
        start = mid+1
        result = mid
    else:
        end = mid - 1
print(result)