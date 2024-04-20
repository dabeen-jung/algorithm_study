'''
[이분탐색] 나무 자르기 (실2)
1. 리스트의 중간 요소를 선택합니다.
2. 찾고자 하는 값과 중간 요소를 비교하여, 탐색의 범위를 '반'으로 줄입니다.
3. 조건을 만족할 때까지 위 과정을 반복

goal: h높이로 잘랐을 경우 남는 것이 m미터 정도를 가져가야 하는데
이 때 h의 최댓값을 구해라 (나무를 굳이 m이상으로 많이 가져가지는 않을거임)
'''

#m: 가져가려는 나무길이
n,m = map(int, input().split())
forest = list(map(int,input().split()))

start,end = 0 ,max(forest)
result = 0 #자르려는 나무 높이

#높이를 작게 자를 수록 -> 나무를 많이 가져감;
while start <= end:
    mid = (start + end) // 2

    high = 0 #가져갈 수 있는 나무길이
    for i in forest:
        if i > mid:
            high += (i-mid)

    #1.가져갈 높이 >= m:
    # m보다는 많이 가져가니, 나무를 더 높게 자르자.
    if high >= m:
        start = mid+1
        result = mid #결과: 베려는 나무 높이
    else:
        end = mid-1

print(result)