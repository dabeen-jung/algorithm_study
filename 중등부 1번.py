
"""
#지능형 기차2
#여기서 나의 잘못은 이미 만들어놓은 배열에 append해서 삽입함
#굳이 하려면 그 자리들에 직접 값을 지정해주자!
#arr=[[0]*2 for i in range (10)]

#for i in range(10):
#    a,b=map(int,input().split())
#    arr.append(a,b)
#print(arr)
    
hap=0
MAX=0

for i in range(10):
    a,b=map(int,input().split())
    hap-=a
    hap+=b
    
    if(hap>MAX):
        MAX=hap
print(MAX)  


#인공지능 시계
h,m,s=map(int,input().split())
n=int(input())
k=n+s


if(k > 59):
    m+=(k//60)
    s=k%60
    
    if(m > 59):
        h+=(m//60)
        m=m%60
        
        if(h>23):
            h=h%24
    print(h,m,s)    
else:
    print(h,m,k)



#간지
n=int(input())

#2013의 'F9'를 0처럼 처음 기준으로 잡기 위해
a=[9,0,1,2,3,4,5,6,7,8] #십간 
b=list('FGHIJKLABCDE') #십이지
k=0

if(n<2013):
    k=(2013-n)%2013
    
    print(b[(k%12)*-1],a[(k%10)*-1],sep='')
else:
    #나머지가 존재
    k=n%2013
    print(b[k%12],a[k%10],sep='')



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
        
#만약 아예 cnt에 해당하는 수가 없을 경우
if(n>cnt):
    print(0)

for i in range(yy+1):
    for j in range(xx+1):
        print(arr[i][j],end=' ')
    print()




    

#1번 카드게임

ar=list(map(int,input().split()))
br=list(map(int,input().split()))
c1,c2=0,0

for i in range(len(ar)):
    if(ar[i]==br[i]):
        continue
    elif(ar[i]>br[i]):
        c1+=1
    else:
        c2+=1

if(c1==c2):
    print('D')
elif(c1>c2):
    print('A')
else:
    print('B')

    
"""
