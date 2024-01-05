# 균형잡힌 세상

#readline은 '\n'을 포함해서 가져옴 -> 줄마다 출력
# 그냥 input이면 개행문자는 자동삭제해서 문제가 안됨
import sys
input = sys.stdin.readline

while True:
    li = input().rstrip('\n')
    stack = []

    if li == '.':
        break

    for v in li:
        if v == '(' or v == '[': # ]
            stack.append(v)

        elif v == ')':
            # )( 이 될 수도 있음
            if len(stack) != 0 and stack[-1]=='(' : # (
                stack.pop()
            else: #
                #만약 빈 stack에 첨부터 ')'부터 넣엇을까봐
                stack.append(v)
                break
        elif v == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(v)
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")
