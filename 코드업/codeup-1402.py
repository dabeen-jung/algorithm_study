#거꾸로 출력하기 
n=int(input())
a=map(int,input().split())
arr=list(map(int,a))

arr.sort(reverse=True)
for i in arr:
    print(i,end=' ')

