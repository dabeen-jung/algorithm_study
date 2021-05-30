#두 용액 4701

from operator import itemgetter
n=int(input())
MAX=2000000000 #최댓값들의 합일경우

ar=list(map(int,input().split()))
ar.sort()

a = 0
b=len(ar)-1
x=0
y =0 #결과 값


while (a<b):
    hap=ar[a] + ar[b]
    
   
    if(abs(hap) <= MAX): #최댓값끼리의 합이 있을 수 있음(=)
        MAX=abs(hap)
        x=ar[a]
        y=ar[b]
        if(hap == 0): #둘의 합이 0일시
            break

     
    #합이 양수냐 ->b감소, 음수냐 -> a를 증가
    #sort로 오름차순이여서.
    if(hap > 0 ):
        b-=1
    else:
        a+=1

print(x,y, sep=' ')
        



