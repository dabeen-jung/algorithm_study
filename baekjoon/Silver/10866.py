# [덱] 덱  (실버4) - 72ms, 34060kb
import sys
input = sys.stdin.readline
from collections import deque

deq = deque()
n=int(input())

for i in range(n):
    arr = input().split()

    if arr[0] == 'push_front':
        deq.appendleft(arr[1])
    elif arr[0] == 'push_back':
        deq.append(arr[1])
    elif arr[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print('-1')
    elif arr[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print('-1')
    elif arr[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print('-1')
    elif arr[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print('-1')
    elif arr[0] == 'empty':
        if deq:
            print('0')
        else:
            print('1')
    else:
        print(len(deq))






