#소수(2581번)
a=int(input())
b=int(input())
hap=0
cnt=0
MIN=10001

for j in range(a,b+1):
    if(j==2):
        if(MIN>j):
            MIN=j
        hap+=j
        cnt+=1
    for i in range(2,j):
        if(j%i == 0):
            break
        if(i==j-1):    #소수확정
            if(MIN > j):
                MIN=j
            hap+=j
            cnt+=1

if(cnt==0):
    print(-1)
else:
    print(hap,MIN,sep='\n')
