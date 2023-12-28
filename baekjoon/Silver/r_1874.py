#[스택] - 스택수열 (실버2)
# 문제를 이해하지 못해서 못풀었던

#규칙: push는 오름차순으로(입력값 상관ㄴ) _ex)1,2,3,4..
# pop은 입력값 순대로 나와야 함
# 436287521 입력값 -> pop 리스트도 이럼
# NO가 나올 때? 값이 pop 될 때 a값 위에 a 보다 작은 값 b가 있는 경우
#ex) 63

import sys
input = sys.stdin.readline

n=int(input())
seq = [int(input()) for _ in range(n)] #수열

stack = []
res = []
cnt = 1
check = 1

for val in seq:
    while True:
        if len(stack) != 0:

            # pop 값과 같은 경우
            if stack[-1] == val:
                stack.pop(len(stack)-1)
                res.append("-")
                break

            else:
                if cnt > n:
                    check = 0
                    break
                stack.append(cnt)
                res.append("+")
                cnt += 1
        else:
            stack.append(cnt)
            res.append("+")
            cnt+=1

    if check == 0:
        print("NO")
        break
if check == 1:
    for v in res:
        print(v)


