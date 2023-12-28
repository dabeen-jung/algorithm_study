# [큐] - 큐(실버4)
# push x
#pop 가장 앞에 있는 정수 빼고 출력, 없다면 -1
# size 큐 내의 갯수, empty 비어있다 1 or 아니면 0
#front 가장 앞정수, 없다 -1
#back 가장 뒤의 수 없다 -1
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
deq = deque()

for i in range(n):
    arr = input().split()

    if arr[0] == 'push':
        deq.append(arr[1])

    elif arr[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print("-1")
    elif arr[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print("-1")

    elif arr[0] == 'pop':
        if deq:
            print(deq.popleft())
        else:
            print("-1")
    elif arr[0] == 'empty':
        if deq:
            print("0")
        else:
            print("1")
    else: #size가 몇 개인가
        print(len(deq))