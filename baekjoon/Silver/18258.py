# [큐] 큐2  (실버4)
#push X: 정수 X를 큐에 넣는 연산이다.
# pop: 가장 앞에 수 빼고 출력, 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 가장 앞에 있는 정수를 출력, 정수가 없는 경우에는 -1을 출력한다.
# back: 가장 뒤에 있는 정수를 출력. 정수가 없는 경우에는 -1을 출력한다.
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
deq = deque()


for i in range(n):
    arr = input().split()

    if arr[0] == 'push':
        deq.append(arr[1])
    elif arr[0] == 'pop':
        if deq:
            print(deq.popleft())
        else:
            print("-1")
    elif arr[0] == 'size':
        print(len(deq))

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
    else: #empty
        if deq:
            print('0')
        else:
            print('1')