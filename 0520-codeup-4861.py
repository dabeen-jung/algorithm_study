
n,m=map(int,input().split())

cnt=0
gst=[]
bst=[]

#여자, 남자별로 나눠서 배열에 학년을 넣어줌.
for i in range(n): 
    a,b=map(int,input().split())
    if(a==0):
        gst.append(b)
    else:
        bst.append(b)


for i in range(1,7): #학년별로 있는 배열(gst등)에서 갯수 세주기
    
    if(gst.count(i)% m !=0):
        cnt+=((gst.count(i)//m)+1)
    else:
        cnt+=(gst.count(i)//m)
        
    if(bst.count(i)% m !=0):
        cnt+=((bst.count(i)//m)+1)
    else:
        cnt+=(bst.count(i)//m)
        
print(cnt)


