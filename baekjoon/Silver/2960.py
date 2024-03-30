'''
[수학] 에라토스테네스의 체
* N보다 작거나 같은 모든 소수를 찾는

'''

n, k = map(int, input().split())
arr = [True] * (n+1) # 0~n 까지
count = 0

for i in range(2, n+1): #2부터 n까지
    if arr[i]:
        for j in range(i, n+1, i): #j: i의 배수
            if arr[j]:
                arr[j] = False
                count += 1

                if count == k:
                    print(j)
                    break
