'''
[그리디] 동전 0 (실 4)

'''

n,k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort(reverse=True)
cnt = 0
val = k

#while문을 돌 필요가 없음
#=> arr 배열 내의 값들에서 해결될 수 있음
for v in arr:
    if v <= val: #범위 안에 들어올 때
        cnt += (val // v)
        val %= v #남은 금액 4200-> 200

    if val == 0: #목표 금액 도달
        break
print(cnt)