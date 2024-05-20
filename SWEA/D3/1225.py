'''
7일차 암호 생성기
1. 첫번째 숫자 -1 한 후, 맨 뒤로 보냄
2. -2한 후 맨뒤로, 그 후는 -3,그 후는 -4,-5까지
* 감소하게 될 결과 값이 0보다 작아지는 경우 걍 0으로 유지시키고 => 종료

'''
from collections import deque

for tc in range(1, 11):
    tn = int(input()) #테스트 케이스 번호
    arr = list(map(int,input().split()))
    brr = deque(arr)
    # print(brr)

    first = brr[0]
    while first != 0:
        for i in range(1, 6):
            first = brr.popleft() - i
            if first <= 0:
                first = 0
                brr.append(first)
                break
            else:
                brr.append(first)

    print('#%d'%(tn), ' '.join(map(str,brr)))