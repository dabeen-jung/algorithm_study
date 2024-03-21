'''
[그리디] 잃어버린 괄호 (실2)
goal: 괄호를 적절히 넣어 결과값을 최소로 만들자
주의: 같은 연산자가 줄이어 나올 수 ㅇ
'''
import re

arr = [int(num) for num in (re.findall('[+-]?\d+', input()))]

res = 0
n = 0
mid = 0
# -가 나오면 -(+들만 나오게)
while n < len(arr):
    if arr[n] < 0:
        if mid == 0:
            mid += arr[n]*-1
        else: # 괄호 닫아주고 -시작 [괄호 닫기]
            res -= mid
            mid = arr[n]*-1
    else:
        if mid > 0: #[괄호 열린 상태]
            mid += arr[n]
        else:
            res += arr[n]

    if n == len(arr)-1 and mid > 0:
        res -= mid
    n+=1


print(res)