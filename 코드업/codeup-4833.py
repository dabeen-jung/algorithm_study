#쇠막대기
a=list(map(str,input()))
#a.reverse()

stack=[]


for i in a:
    stack.append(i)

hap=0
sum=0
for i in range(len(stack)):
    if(stack[i]=='('):
        hap+=1
        #print('결과는 %d 합은 %d',sum,hap)
    else:
        hap-=1

        if(stack[i-1]=='('):
            sum+=hap
            #print('결과는 %d',sum)
        else:
            sum+=1
            #print('결과는 %d',sum)
        
print(sum)

