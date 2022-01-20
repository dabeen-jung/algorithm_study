#경비원 (백준 2564)
#goal: 동근이와 상점 간의 최단 거리의 합
#1:북, 2:남, 3:서, 4:동
#limit: n,w,h<=100 , b > 0

w,h=map(int,input().split())
n=int(input())
arr=[[int(i) for i in input().split()] for j in range(n)]
a,b=map(int,input().split())
print(b)
hap=0
cnt=1 #짝수 건너편은 = 본인-1

if a%2 != 1: #홀수면 건너편=본인+1
   cnt=-1





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
'''    
        
print(hap)
