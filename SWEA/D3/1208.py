'''
[S/W 문제해결 기본] 1일차 - Flatten

주어진 덤프횟수보다 빨리 긑나면 그때 최고-최저 높이 차 계산
goal: 덤프 횟수 끝난 후 최고-최저 높이 차 출력
'''

for tc in range(1,11):
    dump = int(input())
    arr= list(map(int,input().split()))
    # arr.sort(key = lambda x:x[0], reverse = True)
    MAX = -float('inf')
    MIN = float('inf')
    cnt = 0

    while  MAX-MIN != 0: #차이가 없다.(평탄화)
        if cnt == dump:
            break
        MAX = max(arr)
        MIN = min(arr)
        maxIdx = arr.index(MAX)
        minIdx = arr.index(MIN)

        #값 빼주기
        arr[minIdx] += 1
        arr[maxIdx] -= 1

        cnt+=1

    result = max(arr)-min(arr)
    print('#%d %d'%(tc,result))

