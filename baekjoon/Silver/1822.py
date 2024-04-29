'''
[이분탐색] 차집합 (실4)

* goal
A에는 속하면서 집합 B에는 속하지 않는 원소
'''

a,b = map(int, input().split())
A = list(map(int, input().split()))
B = set(map(int, input().split()))
cnt = 0
result = []

for v in A:
    if v not in B:
        cnt += 1
        result.append(v)

result.sort()
print(cnt)
print(' '.join(map(str,result)))