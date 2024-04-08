'''
[투포인터] 수들의 합2 (실4)
goal: 이어지는 수의 합이 M이 되는 경우의 수
'''

n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0 #경우의 수
end = 0
res = 0

for s in range(n):
    # s~end까지 합이 m이 나올 때까지 end를 이동시킴
    while end < n and res < m:
        res += arr[end]
        end += 1 #인덱스 뒤로 이동

    if res == m:
        cnt += 1
    #앞의 수를 빼고 다음 턴으로 넘어감
    res -= arr[s]
print(cnt)
