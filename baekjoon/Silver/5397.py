#[연결리스트 (큐)]  키로거 (실버2)
#goal: 비밀번호를 알아내기

# input: 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표
import sys
from collections import deque
input = sys.stdin.readline

t_c = int(input())
# - : 앞글자 삭제

for i in range(t_c):
    arr = input().strip()
    left = deque()
    right = deque()

    for val in arr:
        if val == '<':
            if left:
                right.appendleft(left.pop())

        elif val == '>':
            if right:
                left.append(right.popleft())

        elif val == '-':
            if left:
                left.pop()

        else:
            left.append(val)

    left.extend(right)

    print(''.join(left) )