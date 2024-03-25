'''
[DP] 퇴사2 (골 5)
조건 : n일까지만 근무
goal: 백준이가 얻을 수 있는 최대 수익을 구하라
'''
import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []
dp = [0] * (n + 1)

for _ in range(n):
    ti, pi = map(int, input().rstrip().split())
    t.append(ti)
    p.append(pi)

#idx + t = 가능한 날의 idx
#idx 날 근무를 할지, pass 할지
'''
최대이익
t가 지나가
'''
for idx in range(n-1,-1,-1):
    #퇴사날을 넘긴다(진행할 수 x)
    if idx + t[idx] > n:
        dp[idx] = dp[idx + 1] #(최댓값,0)을 그대로 저장

    else:
        #다른경우를 방문한 dp vs 그 직전 방문한 dp를 비교 후 -> 최댓값을 삽입
        # 목표는 최댓값을 가지도록 해야함
        dp[idx] = max(p[idx] + dp[t[idx]+idx], dp[idx+1])

#최종적으로 최댓값을 출력할 수 밖에 없음
print(dp[0])

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# t, p = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
# for i in range(1, n + 1):
#     t[i], p[i] = map(int, input().split())
#
# dp = [0 for _ in range(n + 1)]
#
# for i in range(1, n + 1):
#     dp[i] = max(dp[i], dp[i - 1])  # 이전까지의 최댓값
#
#     fin_date = i + t[i] - 1  # 당일 포함
#     # print("i값", i, "findate = ", fin_date)
#     if fin_date <= n:  # 최종일 안에 일이 끝나는 경우
#         # i일부터는 일을 해야하므로 i일에 얻을 수 있는 최댓값이 아닌 i-1일까지 얻을 수 있는 최댓값을 구한다
#         dp[fin_date] = max(dp[fin_date], dp[i - 1] + p[i])
# print(max(dp))