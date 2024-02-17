'''
[재귀] 곱셈 (실1)
goal: A를 B번 곱한 수를 C로 나눈 나머지
조건: 2,147,483,647 이하의 자연수

'''

import sys
input = sys.stdin.readline

a,b,c = map(int, input().rstrip().split())

'''
a =2, b=32 [짝수일 때]
* why 이 방법? 
즉, 재귀는 시간초과 O(n) => 시간복잡도를 줄이자 => O(logN)

1. (?)^2 = 원본값(짝수의 경우)
2. (A^5)^2 * A = A^11 (홀수의 경우)

문제 해결 목표: 눌 수 없을 때까지 나눠주고 재귀함수를 걸쳐 나온 다음에 마지막에 나머지 처리
)^2 라는건 본잉ㄴ을 한 번 더 곱해준거잖음
'''
def fx(a,b,c):
    if b == 1: #
        # print(a%c)
        return a % c

    elif b % 2 == 0: #짝수
        return (fx(a,b//2, c) **2) %c

    else : #홀수
        return ((fx(a, b//2, c)**2)*a) %c

print(fx(a,b,c))