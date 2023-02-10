
#최댓값

a=[[int(i) for i in input().split()] for j in range(9)]
MAX=0
x,y=0,0

for i in range(9):
    for j in range(9):
        
        if(a[i][j] > MAX):
            MAX=a[i][j]
            x,y=i+1,j+1
print(MAX)
print(x,y)

