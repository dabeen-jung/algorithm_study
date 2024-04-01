'''
[그리디] 수 묶기(골4)
아예 묶이지 말던, 한 번만 묶이던 해야함

[조건] : -1000 <= 값 <= 1000

<음수가 있다>
1. 음수끼리 더하는게 훨씬 나음
<양수다>
1. 높은 수끼리 곱함
+) 1이면 더해라


*goal: 묶은 수는 곱하고 합하는 등 해서 '최대합'을 만들어라
'''

n = int(input())
pos = []
neg = [] #음수

cnt,result = 0,0

#1. 음수,양수기준으로 배열 입력
for _ in range(n):
    num = int(input())

    if num > 1: #1은 더하는게 더 나음
        pos.append(num)
    elif num <= 0:
        neg.append(num)
    else: #1일때
        result += 1

#2. 음수배열 -> 오름차순, 양수배열 -> 내림차순
pos.sort(reverse=True)
neg.sort()  #ex) -100,-50,-4,-1

# 3. 양수배열 처리(곱하기)
while len(pos) > 1: #홀수일 수 있으니 그건 따로 처리할거임
    result += (pos.pop(0) * pos.pop(0))
if pos: #홀수개였다면
    result += pos[0]

# 음수 처리
while len(neg) > 1:
    result += (neg.pop(0) * neg.pop(0)) #앞에서부터
if neg:  # 홀수 개인 경우
    result += neg[0]

print(result)

