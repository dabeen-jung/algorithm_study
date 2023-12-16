#다시 풀기 _ 골드3
'''
공주님의 정원
https://haesoo9410.tistory.com/193
list를 정렬을 하게 될때 x:() 괄호안에 튜플형식으로 집어넣는다.
-x[0]이면 내림차순으로 하겠다는 뜻이다.
'''

n=int(input())
arr=[]
#arr=[[]  for i in range(n)]
ar=[[int(i) for i in input().split()] for _ in range(n)]
for i in range(n):
    for j in range(0,4,2):
        if j==0:
            arr.append([ar[i][j]*100 + ar[i][j+1]])
        else:
            arr[i].extend([ar[i][j]*100 + ar[i][j+1]])

arr.sort(key = lambda x:( x[0], -x[1]))


cnt=0
fin=301 #기준
comps = []
i=0

while(1):
    s,f=arr[i][0],arr[i][1]

    if fin>=1130 :
        break
    if s<=fin :
        comps.append(f)
        
    if s>fin or i == len(arr)-1:    #순번이 마지막일때, 기준을 한참 벗어나서 max처리 해줘야 함
        if comps==[]:
            break
        fin=max(comps)
        cnt+=1
        comps=[]
        if i == len(arr)-1: #fin을 재설정 함으로써 s,f 값을 다시 넣고 재정비
            break
        i-=1
    i+=1

if fin<1130:
    cnt=0

print(cnt)
    

        
    
