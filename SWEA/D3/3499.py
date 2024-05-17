'''
3499 퍼펙트 셔플

덱을 절반 나눔 -> 나눈 것들을 교대로 뽑아 새로운 덱을 생성
N이 홀수? 교대로 : 먼저 놓는 쪽이 1장 더 있다 (3:2)

goal: 퍼펙트 셔플시 순서 출력
'''
from collections import deque

for tc in range(1, int(input())+1):
    N = int(input()) #카드 수
    arr = list(input().split())
    re = True #짝수
    #카드 위치 정해짐
    if N%2 == 1: #홀수
        left = deque(arr[:(N//2)+1]) #얘가 하나더 많음
        right = deque(arr[(N//2)+1 : ])
        re = False
    else:
        left = deque(arr[ : (N//2)])
        right = deque(arr[(N//2) : ])


    cnt = 0
    result = []
    print('#%d'%(tc), end =' ')

    for i in range(N//2) :
        print(left.popleft(), right.popleft(), end=' ',sep=' ')

    if not re:
        print(left.popleft())
    else:
        print()