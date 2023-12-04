#랜선 자르기(결정 알고리즘)
#n 개 이상의 갯수로 동일한 길이의 랜선을 만들어라
#goal: n개를 만들 수 있는 최대 랜선길이

k,n = map(int,input().split())
arr = [int(input()) for _ in range(k)]
arr.sort()
st = 1
lt = arr[k-1]
res = 0

while st<=lt:
    mid = (lt+st)//2
    cnt = 0
    for i in range(k):
        cnt += (arr[i]//mid)

    if cnt < n: #mid가 너무 크다
        lt=mid-1
    else:
        if res < mid:
            res = mid
        st=mid+1

print(res)


