'''
[그리디] 보물 (실1)
S = A[0] × B[0] + ... + A[N-1] × B[N-1]

goal: S의 값을 가장 작게 하기위해, A 수만 재배열해라(단,B는 재배열해선 안된다)
'''

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

#8,7,3,2,1 [0,1,1,1,6]
#2,7,8,3,1

A.sort()
S = 0
for i in range(N):
    # B가장 큰 값 * A 가장 작은 값
    S += A[i] * max(B)
    #값을 삭제 할 때는 remove
    B.remove(max(B))

print(S)