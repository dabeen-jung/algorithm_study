#M_점수계산

n=int(input())
a=[int(i) for i in input().split() ]
res=0
lst=0
k=1

for i in (a):
    if(i==1):
        if(lst==1):
            k+=1
        else:
            k=1
        lst=i
        res+=(i*k)
    else:
        lst=0
        
print(res)
