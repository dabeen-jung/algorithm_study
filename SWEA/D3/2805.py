'''
농작물 수확하기
'''

for tc in range(1,int(input())+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    # print(arr)
    mid = N//2
    result = 0

    for i in range(N):
        if i <= mid:
            for j in range(mid-i, mid+i+1):
                result += arr[i][j]
        else:
            for j in range(i-mid, N + mid - i):
                result += arr[i][j]

    print('#%d %d'%(tc,result))
