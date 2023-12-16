#숫자야구 (실버3)
'''
조건) 서로 다른 3자리 수
i) 같은 자리, 같은 숫자-> 스트라이크
ii) 같은 숫자 -> 볼
'''

n=int(input())
arr=[]
brr=[]  #통과 결과만

cnt=0

for i in range(n):
    k=list(map(int,input().split()))
    arr.append(k)

for i in range(123,988):    #답을 가정(기준치)
    aa,bb,cc=i//100,(i//10)%10,i%10
    #f=1
    c=0
    
    if aa==bb or aa==cc or bb==cc:
        continue
    
    for j in range(n):  #조건별로 통과하는지 본다
        s,b=0,0 #strike, ball 초기화
        for num in str(arr[j][0]):
            if str(i).count(num)>=1:
                if str(i).find(num) == str(arr[j][0]).find(num):
                    s+=1
                else:
                    b+=1
        if s==arr[j][1] and b==arr[j][2]:
            c+=1
            continue
        else:
            #f=0
            break
                
        
    if c==n:
        cnt+=1
                
print(cnt)
                
        
        

