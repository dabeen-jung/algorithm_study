# 두 수의 합 (실버3) - 다시 풀기
# 해시테이블이나 집합(set)을 쓰는걸 추천
#시간복잡도 O(n)이라

# 혹은 투 포인터를 쓰길 추천한다고 함. 배열로 못 만들까?

n = int(input())
arr=list(map(int,input().split()))
x = int(input())
cnt = 0

#시간초과 남
# for i in range(n-1):
#     for j in range(i+1,n):
#         if arr[i]+arr[j] == x:
#             cnt+=1
#
# print(cnt)

#시간 초과 남
for num in arr:
    if x - num in arr:
        cnt+=1

print(cnt)