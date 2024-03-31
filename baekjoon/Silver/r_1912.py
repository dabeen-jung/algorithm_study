'''
[Dp] 연속합 (실2)
* 임의의 수열 중 '연속된 몇 개의 수'만을 선택해 => 가장 큰 합을 구해라

'''

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]

for i in range(1,n):
    dp[i] = max(arr[i] , dp[i-1] + arr[i])
    # print(dp[i])
# print(dp)
print(max(dp))