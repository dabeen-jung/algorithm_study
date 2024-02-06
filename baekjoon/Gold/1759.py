'''
[백트래킹] 암호 만들기

1. 서로 다른 L개의 알파벳 소문자들로 구성
2. 최소 1개_ 모음(a, e, i, o, u)과
2. 최소 2개의 자음으로 구성
3. 암호는 알파벳이 증가하는 순(사전순)대로 배열 (abc(0)  bac(x))

중복 x
'''

import sys
input = sys.stdin.readline

# 서로 다른 L개로 구성된 모음 / 사용할 문자 종류
L,C = map(int, input().split())
arr = list(input().split())
# print(arr)
arr.sort()


result = []
# jaem, moem = 0,0

# 알파벳 순으로 뽑을거임(중복x): 2자음 + 1모음 <=L
def rep(start ,moem, jaem, depth):
    if depth == L: #L이 되면 중단
        if jaem >= 2 and moem >=1:
            print(''.join(map(str,result)))
        return

    for i in range(start,C):
        # depth가 마지막 직전인데, 현재 자음2+모음1이 안되는가?
        if arr[i] in ['a', 'e', 'i', 'o', 'u']:  # 모음
            if depth == L-1 and jaem < 2: #마지막 전 값
                continue
            result.append(arr[i])
            rep(i+1,moem+1,jaem ,depth+1)
            # moem-=1
            result.pop()

        else:
            # 마지막 전 값의 최소 자음 모음 조건 충족하는지 확인
            if depth == L - 1 and moem < 1:
                continue
            result.append(arr[i])
            rep(i+1 ,moem ,jaem+1 ,depth+1)
            # jaem -= 1
            result.pop()

rep(0,0,0,0)