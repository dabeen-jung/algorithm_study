#스택
import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    val = input().split()

    if val[0] == 'push':
        stack.append(val[1])

    elif val[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif val[0] == 'size':
        print(len(stack))
    elif val[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else: #top일때
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

