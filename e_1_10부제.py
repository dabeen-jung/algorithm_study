"""

#백설공주와 난장이


arr=[]
for i in range(7):
    n=int(input())
    arr.append(n)
arr.sort(reverse=True)

for i in range(2):
    print(arr[i])



#대표값2

hap=0
arr=[]

for i in range(5):
    n=int(input())

    arr.append(n)#리스트 
    hap+=n
arr.sort()
print(hap//5)
print(arr[2])

#대표값2 다른 방
import statistics
arr=[]
hap=0
for i in range(5):
    n=int(input())

    arr.append(n)#리스트 
    hap+=n

print(hap//5)
print(statistics.median(arr))


#홀수

hap=0
MIN=100
for i in range(7):
    a=int(input())

    if(a%2==1):
        hap+=a
        if(MIN>a):
            MIN=a
if(hap==0):
    print('-1')
else:
    print(hap,MIN,sep='\n')



#최대값 -> 파이썬만 쓸 수 있는 방
'''
a=[]

for i in range(9):    
    a.append(int(input()))

print(max(a),a.index(max(a))+1,sep='\n')
'''

#최댓값 -> 다른 곳에서는 일케 씀
m = 0
idx = 0
for i in range(9):    
    t = int(input())
    if m < t:
        m = t
        idx = i + 1

print(m,idx,sep='\n')


#약수구하기
n,k=map(int,input().split())
arr=[1,n]

for i in range(2,n):
    if(n%i == 0):
        arr.append(i)

arr.sort()
#print(arr)
print(arr[k-1])


#윷놀이
for i in range(3):
    hap=sum(map(int,input().split()))

    if(hap==0):
        print('D',end='')
    elif(hap==1):
        print('C',end='')
    elif(hap==2):
        print('B',end='')
    elif(hap==3):
        print('A',end='')
    else:
        print('E',end='')


#검증수
n=list(map(int,input().split()))
res=0

for i in n:
    res+=(i**2)

print(res%10)



#지능형 기차

res=0
MAX=0
for i in range(4):
    a,b=map(int,input().split())
    res-=a
    res+=b
    if(MAX < res):
        MAX=res
print(MAX)


#오븐시계
a,b=map(int,input().split())
tt=int(input())
m=b
h=a
m+=tt

if(m//60 > 0):
    #print('%d'%(m))
    h+=(m//60) #시 세팅
    m=(m%60)    #분 세팅
    
    #print('%d'%(h))
    if(h>23):
        h=(h//25)
        
print('%d %d'%(h,m))
    

#그릇
a=input()
cnt=10

for i in range(1,len(a)):
    if(a[i]==a[i-1]):
        cnt+=5
    else:
        cnt+=10
print(cnt)




#정올 초1
#10부제

cnt=0

n=int(input())
a=list(map(int,input().split()))

for i in a:
    if(i == n):
        cnt+=1

print(cnt)
    
    
#정올 초_1
#과자

k,n,m=map(int,input().split())

res=k*n

if(res>=m):
    print('%d'%(res-m))
else:
    print('%d'%(m-res))

"""
