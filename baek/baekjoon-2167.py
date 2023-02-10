
#긴급 알고리즘 문제(dp 동적프로그래밍 문제)
#백준 2167번 2차원 배열의 합

n,m=map(int,input().split())
ar=[]
#ar=[[0]*(m+1) for i in range(n+1)]  #기본 배열
sum_ar=[[0]*(m+1) for _ in range(n+1)]  #누적합 배열


for i in range(1,n+1):  #기본배열 값 세팅
    #tt=0
    a=[int(j) for j in input().split()]
    #a=list(map(int,input().split()))
    ar.append(a)
    '''for j in a:
        
        tt+=1
        ar[i][tt]=j'''
        
for i in range(1,n+1):  #누적합 세팅
    for j in range(1,m+1):
        sum_ar[i][j]=sum_ar[i-1][j]+sum_ar[i][j-1]-sum_ar[i-1][j-1]+ar[i-1][j-1]
        #print(sum_ar[i][j],end=' ')
    #print()


k=int(input())


for _ in range(k):
    i,j,x,y=map(int,input().split())
    if(i==x and j==y):
        res=ar[i-1][j-1]
        print("%d"%res)
    else:
        res=sum_ar[x][y] - sum_ar[i-1][y]-sum_ar[x][j-1]+sum_ar[i-1][j-1]
        print("%d"%res)

