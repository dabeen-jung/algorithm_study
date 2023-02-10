
"""
#줄세우기


n=int(input())  #학생 수
arr=list(map(int,input().split()))
res=[]
k=1
tt=0 #입력할 값


for i in (arr):
    tt+=1   #학생번호
    if(i==0):
        res.insert(i,tt)
    else:
        res.insert(len(res)-i,tt)
    
for i in res:
    print(i, end=' ')

#곱셈
#숫자를 리스트 안에 각각 넣는 방법
#n=input()
#a=list(n)

a = 0
b = []
hap=0
res=0 #곱의 합
for i in range(2):
    n=int(input())

    #숫자를 str로 바꾸고 하나씩 int형으로
    #변환해서 리스트에 넣어줌
    if(i==0):
        a = n
    else:
        b = list(map(int,str(n)))
        b.reverse()

for i in range(4):
    if(i==3):
        print(hap)
    else:
        res=a*b[i]
        hap+=res*(10**i)
        print(res)
    



#숫자의 개수

#1.while 문으로 %10씩 해주는 방법

b=[0 * i for i in range(10)]
res=1 #숫자 결과
cnt=0
for i in range(3):
    n=int(input())
    res*=n
    
while(1):
    b[res%10] +=1 #해당 칸에 갯수 증가
    res=res//10 #해당 res 정비
    if(res == 0):
        break

for i in range(10):
    print(b[i])

#2. count()함수
k=1
for i in range(3):
    n=int(input())
    k*=n
    
# k를 str형식으로     
k=str(k)

for i in range(10):
    print(k.count(str(i)))


  

#색종이
n=int(input()) #색종이 갯수

arr=[[0]*100 for i in range(100)]
cnt=0

for i in range(n):
    #(x,y) 좌표로

    a,b=map(int,input().split())

    for j in range(b,b+10):
        for k in range(a,a+10):
            if(arr[j][k]==1 or (j>100 or k >100)):
                continue
            arr[j][k]=1
            cnt+=1

print(cnt)



#떡 먹는 호랑이
n=0 #무사히 넘어온 날
k=0 #n날에 준 떡 갯수

#구해야 하는것: 첫 날 떡의 갯수, 둘쨋날 떡의 갯수

def solution(n,k):
    for i in range(k): #첫 번째 떡의 갯수 세팅
        
        for j in range(i, k): #두번째 떡의 갯수 세팅
            a,b=i,j
            
            for _ in range(n-2):
                #앞의 두 날(i,j)을 뺀 마지막 날까지..
                c=a+b
                a,b=b,c
                
            if c==k:
                #결과적으로 떡의 갯수가 마지막이랑 같은가
                print(i)
                print(j)
                return
            
n,k=map(int,input().split())
solution(n,k)
            


#수열 (다시 풀어보기)
n=int(input())
ar=list(map(int,input().split()))

t=1 #1,2,3 오름차순 변수
g=1 #3,2,1 내림차순 변수
cnt=1 #길이
MAX=0

for i in range(1,n):
    if(ar[i] == ar[i-1]):
        #두 변수 다 값이 증가
        t+=1 
        g+=1
    elif(ar[i] > ar[i-1]):
        #오름차순의 경우
        t+=1
        g=1
    else:
        #내림차순의 경우
        t=1
        g+=1

    if(MAX < max(t,g)):
        MAX=max(t,g)

if(MAX < 2):
    #MAX가 3도 아니고, 2 아래=> 무조건 2로 출력
    print(2)
else:
    print(MAX)




#주사위 게임
n=int(input())
MAX=0
hap=0

for i in range(n):
    arr=[0*i for i in range(7)] # 1-6 인덱스로 넣을 것
    a,b,c=map(int, input().split())
    
    arr[a]+=1
    arr[b]+=1
    arr[c]+=1

    
    
    #가장 큰 눈 비교 대상
    RMAX=0
    cnt=0
    for i in range(1,len(arr)):
        if(arr[i]==3):
            hap=10000+(i*1000)
            break
        elif(arr[i]==2):
            hap=1000+(i*100)
            break
        elif(arr[i]==1):
            if(RMAX < i ):
                RMAX=i
                cnt+=1
    #모두 다른 눈일시            
    if(cnt==3): 
        hap=RMAX*100

    #print(arr,hap, sep=' ')

    #가장 많은 상금을 받은 이의 상금 출력
    if(MAX < hap):
            MAX=hap

print(MAX)

    

#나는 학급회장이다.
from operator import itemgetter

n=int(input())
#[몇 , 1점,2점,3점,총합]
r=[[1,0,0,0,0],[2,0,0,0,0],[3,0,0,0,0]]


for i in range(n):
    a,b,c=map(int,input().split())
    r[0][4]+=a
    r[1][4]+=b
    r[2][4]+=c

    #해당 인덱스 올리기
    r[0][a]+=1
    r[1][b]+=1
    r[2][c]+=1
    

r.sort(key=itemgetter(2), reverse=True)
r.sort(key=itemgetter(3), reverse=True)
r.sort(key=itemgetter(4),reverse=True)

#print(r)

for i in range(3,1,-1):
    MAX=r[0][i]#총합

    
    if MAX==r[1][i] and MAX==r[2][i]:
        if(i==2):
            print('0 %d'%(r[i][4]))
            break
        
    #최고점과 값이 같지 않음 -> 값이 작음
    elif MAX != r[1][i]:
        print('%d %d'%(r[0][0],r[0][4]))
        break
    
    


#싸이클
a,b=map(int,input().split())
arr=[]
ori=a


while(1):
    a=(a*ori)%b

#arr에 아무것도 없다고 오류뜨진 않는다!
#index -> 아무것도 없으면 오류뜸
    
    if a in arr:
        break
    arr.append(a)

print(len(arr))


#3번 덩치

n=int(input())
arr=[]
r=[]

for i in range(n):
    a=list(map(int,input().split()))
    arr.append(a)

for i in range(n):
    x=arr[i][0]
    y=arr[i][1]
    ra=1

    for j in range(n):
        p=arr[j][0]
        q=arr[j][1]
        
        
        #나보다 상대가 더 큰 경우.
        if(y-q < 0 and x-p < 0 ): 
            ra+=1
    r.append(ra)
    #print(r)
        
print(r)

    


#2번 자리배정

c,r=map(int,input().split())
xx,yy=c,r  #c,r 저장해주기 
n=int(input())

cnt=0 
arr=[[0]*(c+1) for i in range(r+1)]

#시작 수
x=1
y=r
di=-1

while(1):
    for i in range(r):
        y=y+di
        cnt+=1
        arr[y][x]=cnt
        
        if(n == cnt): #해당 자릿수
            print('%d %d'%(x,yy-y))

    #세팅 
    r-=1
    c-=1
    # - + + - 순으로 넘어감
    di*=-1 
    
    for i in range(c):
        x=x+di
        cnt+=1
        arr[y][x]=cnt

        if(n==cnt): #해당 자릿수
            print('%d %d'%(x,yy-y))            
        
    if(cnt == xx*yy): #전체 다 돌았음
            break

        
#1번 세로 읽기

arr=[]
MAX=0
res=""

for i in range(5):
    n=input()

    #입력받은 수의 길이가 가장 긴 것 찾기.
    if(MAX<len(n)):
        MAX=len(n)
    arr.append(n)
    

for i in range(MAX):
    for j in range(5):
        
        if(len(arr[j]) <= i):
            continue
        res+=arr[j][i]

print(res)
"""
