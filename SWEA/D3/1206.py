'''
1일차 -view

조망권 = 양쪽 모두 거리가 각각 2이상으 ㅣ공간이 확보되어야 함
goal: 조망권 확보된 세대 수

69+42
내 양 옆으로 2칸씩 나보다는 작아야 함, 이 범위 내에서 나 다음으로 큰
장애물이 있다면 그것을 기준으로 자름
'''


for t in range(1,11):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0

    for i in range(2,n-2):
        MAX = max(arr[i-2:i+3])
        # print(MAX)
        if MAX == arr[i]: #성공
            brr = sorted(arr[i-2:i+3],reverse = True) #내림차순
            diff = brr[1] #비교군
        else:
            continue
        result += (arr[i] - diff)

    print('#%d %d'%(t,result))