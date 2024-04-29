'''
[이분탐색] 용액 (골5)

- 산성용액  + 알칼리 or 산산 or 알알 => 0에 가까운 수가 나오면 됨
'''


import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().split()))

# 투포인터
lf = 0
rt = n - 1

result = float("inf")
res_lf = 0
res_rt = n - 1

while lf < rt:
    temp = arr[lf] + arr[rt]

    #큰 경우, 갱신해서 값 재조정 및 위치 기억해놓기
    if abs(temp) < result:
        res_lf = lf
        res_rt = rt
        result = abs(temp)

    if temp == 0: #0 발견
        break
    elif temp < 0:
        lf += 1
    else:
        rt -= 1

print(arr[res_lf], arr[res_rt])

#이분탐색
# answer = float("inf")
# res_lf = 0
# res_rt = n-1
#
# for idx in range(n-1):
#     start = idx + 1
#     end = n-1
#
#     while start <= end:
#         mid = (start + end) // 2
#         temp = arr[mid] + arr[idx]
#
#         if abs(temp) < answer:
#             answer = abs(temp)
#             res_lf = idx
#             res_rt = mid
#
#         if temp == 0:
#             break
#         elif temp < 0:
#             #작다.
#             start = mid + 1
#         else:
#             end = mid - 1
# print(arr[res_lf], arr[res_rt])