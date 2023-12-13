#경비원 (백준 2564)
#goal: 동근이와 상점 간의 최단 거리의 합
#1:북, 2:남, 3:서, 4:동
#limit: n,w,h<=100 , b > 0


hap=0
w,h=map(int,input().split())
n=int(input())

arr=[[int(i) for i in input().split()] for j in range(n+1)]


#수정본
#좌표 새로이 나열
for i in range(n+1):   
   if arr[i][0]==1:
      continue
   elif arr[i][0]==4:
      arr[i][1]=w+arr[i][1]
      
   elif arr[i][0]==2:
      arr[i][1]=w+h+(w-arr[i][1])

   else :
      arr[i][1]=2*(w+h)-arr[i][1]

a,b=arr[n][0],arr[n][1]  #X의 위치

for i in range(n):   #끝은 x위치로 배제할 것
   a1=abs(b-arr[i][1])
   a2=abs(2*(w+h) - a1)
   hap+=min(a1,a2)

print(hap)


'''
for d,st in arr:
    if a==2:  #상점이 옆면임
        if d==3:
            hap+=b+(h-st)
        elif d==4:
            hap+= (w-b) + (h-st)

        elif d==1: #반대편
            t1 = (w-b)+ h + (w-st)
            t2 = b + h + st
            print(t1,t2,sep=' ')
            hap+=min(t1,t2)
        else:
            if st>b:
                hap+=st-b
            elif st<b:
                hap+=b-st
            else:
                hap+=b
        print(hap)
        
    elif a==4:
        if d==2:
            hap+= (w-st) + (h-b)
        elif d==1:
            hap+= b+(w-st)
        elif d==3:
            t1= w + (h-b) + (h-st)
            t2= w + b + st
            hap+=min(t1,t2)
        else:
            if st>b:
                hap+=st-b
            elif st<b:
                hap+=b-st
            else:
                hap+=b
        print(hap)
    
    elif a==3:
        if d==2:
            hap+= (h-b) + st
        elif d==1:
            hap+= b+st
        elif d==4:
            t1= w + b + st
            t2= w + b + st
            hap+=min(t1,t2)
        else:
            if st>b:
                hap+=st-b
            elif st<b:
                hap+=b-st
            else:
                hap+=b
        print(hap)
    
    else:
        if d==3:
            hap+= b + st
        elif d==4:
            hap+= (w-b) + st
        elif d==2:
            t1= (w-b) + h + (w-st)
            t2= b + h + st
            hap+=min(t1,t2)
        else:
            if st>b:
                hap+=st-b
            elif st<b:
                hap+=b-st
            else:
                hap+=b
print(hap)
'''    
        

