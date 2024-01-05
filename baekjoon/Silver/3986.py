#좋은 단어 (실버4)
# 같은 단어끼리 짝을 지을 것임 (선끼리 교차하지 않아야함)
# goal: 한 줄에서 교차가 되지 않게하여, 결국 모든 짝을 찾아 텅 비는 경우의 갯수

import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for i in range(n):
    arr = input().rstrip()
    stack = []

    for v in arr:
        if len(stack) == 0:
            stack.append(v)

        else:
            if v == 'A':
                if stack[-1] != 'A': #마지막과 같은가? AA인가 BA인가
                    stack.append(v)
                elif stack[-1] == 'A': #겹친다 A A이다.
                    stack.pop() #짝을 이뤄서 나감

            elif v == 'B':
                if stack[-1] != 'B':
                    stack.append(v)
                elif stack[-1] =='B':
                    stack.pop()

    if len(stack) == 0:
        cnt += 1
        # print("stack",stack)

print(cnt)



