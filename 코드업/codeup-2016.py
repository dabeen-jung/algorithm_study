#2016 천단위 구분기호
n=int(input())
a=list(map(int,input()))
a.reverse()

stack=[]
cnt=0
for i in a:
    cnt+=1
    stack.append(i)
    
    
    if(cnt%3==0 ):
        #cnt=0
        if(n==cnt):
            continue
        stack.append(',')
        
            
    


for i in range(len(stack)):
    print(stack.pop(),end='')

print()
print()

