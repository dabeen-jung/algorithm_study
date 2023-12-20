#나머지 합(구간합) (골드3)
# 연속 구간합이 m으로 나누어 떨어져야함(나머지 ==0)
# 이런 상황일 때 몇 쌍의 갯수인지
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(map(int,input().split()))

#구간합 배열
matrix = [0]*n
# 구간합을 %m 나머지들의 갯수 측정
res = [0]*m
count = 0

#1. 누적합
matrix[0] = A[0]
for i in range(1,n):
    matrix[i] = matrix[i-1] + A[i]

#2. 누적합 배열을 m으로 나눈 경우 계산
for i in range(n):
    nmg = matrix[i]%m
    if nmg == 0: # 증가
        count+=1
    res[nmg]+=1

#3. 나머지가 나온 배열에서 같은 수가 나온개 2개이상이면
# 그 두 개를 뽑은 경우도 count해줘야함
for i in range(m):
    if res[i] > 1: # 2개를 뽑아서 3C2 이런걸 해줌 => 나머지가 0인게 총5번 나왔다, 이런 식
        count += (res[i] * (res[i]-1) // 2)

print(count)
