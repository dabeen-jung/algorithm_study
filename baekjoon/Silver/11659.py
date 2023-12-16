#구간 합 구하기4 (실버3)
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))

#누적합 list
prefix_sum = [0]

for i in arr:
    prefix_sum.append(prefix_sum[-1]+i)

for _ in range(m):
    a,b = map(int,input().split())

    print(prefix_sum[b] - prefix_sum[a-1])


#시간초과
# O(n*m)이 됩니다. 이는 최악의 경우 약 10,000,000,000번의 연산을 수행
# for i in range(m):
#     a,b = map(int,input().split())
#
#     if a == b:
#         print(arr[a-1])
#     else:
#         print(sum(arr[a-1:b]))
#         #res.append(sum(range(arr[1],arr[4]))) => 연속된 수여야 됨

