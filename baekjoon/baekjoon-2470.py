#두 용액 4701
from operator import itemgetter
n=int(input())
MAX=1000000000

ar=list(map(int,input().split()))
ar.sort()

a=0
b=n-1
print(ar)


while(a < b): #인덱스가 MAX보다 큰 순간.
    
    hap=abs(ar[a] + ar[b])
    #print('0. MAX= %d hap=%d, ar[a]= %d, ar[b]=%d'%(MAX,hap,ar[a],ar[b]) )


    if((ar[a]+ar[b]) == 0): # 용액이 같을 경우
        #print('1. M= %d, N=%d'%(ar[a],ar[b]))
        break

    # 용액의 합>0 -> b-- (양수를 작은 수로 대체)
    elif((ar[a] + ar[b]) > 0):
        if (abs(ar[a] + ar[b]) < MAX):
            MAX=abs(ar[a] + ar[b])

            # b-- 인덱스 적용시,
            #이전 MAX보다 작아선 안됨, a==b가 되어선 안된다.
            if(abs(ar[a] + ar[b-1]) < MAX and a != b-1 ):
                b-=1 #b 인덱스를 -증가

            else:
                break

    # 용액의 합 < 0 -> a++ (음수를 작은 수로 대체 )  
    elif((ar[a]+ar[b]) < 0):
        if (abs(ar[a] + ar[b]) < MAX):
            MAX=abs(ar[a] + ar[b])

            if(abs(ar[a+1] + ar[b]) < MAX and a+1 != b ):
                a+=1
            
            else:
                #print('4. 이것은 M= %d, N=%d'%(ar[a], ar[b]))
                break
            
     
print(ar[a],ar[b],sep=' ')


