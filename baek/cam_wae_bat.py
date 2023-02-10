#참외밭
#
#-> (1) <-(2) 남쪽(3) 북쪽(4)

arr=[]
w,h=0,0     #MAX값
m_w,m_h=0,0
result=0

n=int(input())

for i in range(6):
    a,b=map(int,input().split())
    arr.append((a,b))
    if a==1 or a==2:
        if w<b:
            w=b
    elif a==3 or a==4:
        if h<b:
            h=b


for i in range(6):
    if i==0:
        result=arr[5][1] + arr[i+1][1]
    elif i==5:
        result=arr[i-1][1] + arr[0][1]
    else:
        result=arr[i+1][1] + arr[i-1][1]

    if arr[i][0] == 1 or arr[i][0]==2:
        if result==h :  #작은 가로 구하기
            m_w=arr[i][1]
            continue
        
    if arr[i][0] == 3 or arr[i][0]==4:
        if result==w :  #작은 세로 
            m_h=arr[i][1]
            continue
            
    
print(((w*h)-(m_w*m_h))*n)
