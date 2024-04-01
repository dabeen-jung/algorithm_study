'''
[dp] 가장 큰 증가하는 부분 수열 (실2)
* 합이 최대가 될 수 있게 ,'점차' 증가하는 모습을 보이는 순열을 만들라
=>{1,2,50,60}
'''

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]

for i in range(1,n):
    # 1. 뽑힌 수들은 '증가하는' 양식을 띄워야 하므로 일일히 다시 비교
    for j in range(i):
        if arr[i] > arr[j]:
            # 연이어서는 아니고, 몇 칸 넘어서 더해주는게 나을지 (비교)
            dp[i] = max(dp[i], arr[i] + dp[j])
        else:
            dp[i] = max(dp[i] , arr[i])

print(max(dp))
