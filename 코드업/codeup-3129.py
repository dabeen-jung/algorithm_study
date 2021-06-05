
a=list(map(str,input()))

stack=[]

a.reverse()
for i in (a):
    stack.append(i)


def f(a):
    #cnt=0
    #tnt=0
    hap=0
    for i in range(len(stack)):
        
        if(stack.pop()==')'):
            if(hap==0):
               # print('hap=%d',hap)
                return print('bad')
            hap-=1
            #print('tnt=%d'%tnt)
            
        else:
            hap+=1
            #print('cnt=%d',cnt)
        
    if(hap==0):
        #print('hap=',hap)
        return print('good')
    else:
        #print('hap=',hap)
        return print('bad')

f(a)




