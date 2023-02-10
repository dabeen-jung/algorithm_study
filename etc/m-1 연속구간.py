#m_1 연속구간

'''
2차원 배열을 만드는 다양한 방법...
a=[]

for i in range (3):
    n=input()
    a.append([int(j) for j in n])
  
    
'''
a=[]
#t=0
hap=1
MAX=1

for i in range (3):
    a.append([])
    n=input()
    for j in n:
        a[i].append(int(j))
    


for i in range(3):
    
    for j in range(1,len(a[i])):
        if(a[i][j]==a[i][j-1]):
            hap+=1
            if(MAX < hap):
                MAX=hap
                #print('현 %d, hap %d, MAX %d'%(j,hap,MAX))
        else:
            hap=1
    print(MAX)
    MAX=1
    hap=1
#print(a)
    
