#대푯값 백준(2592번)
#딕셔너리...참고
hap=0
cnt=0
check=0
h=[]

'''#리스트 이용 방법
a=[]
max=0
maxt=0
for i in range(10):
    t=int(input())
    hap+=t
    #a...[10,1],[]
    for j in range(len(a)):
        if(a[j][0] == t):
            check=1
            a[j][1]+=1
            break
    if (check==0):
        a.append([t,1])
    check=0

    for k in range(len(a)):
        if(max < a[k][1]):
            max=a[k][1]
            maxh=a[k][0]
            
print(hap//10, maxh,sep='\n')''' 



'''
a=[]
#리스트 방법 1
for i in range(10): #0,1,2...
    h=int(input())
    hap+=h
    print('h= %d, i= %d'%(h,i))

    for t in range(len(a)): #0,1,2,3,    
        if(a[t][0] == h):
            a[t][1]+=1
            check=1
            break
    if(check==0):
        a.append([h,1])
    check=0

    print(hap//10, )


print(a)'''


'''#딕셔너리1
a=dict()
maxh=0
max=0
maxi=0

for i in range(10):
    t=int(input())
    hap+=t

    if t in a:  #a 딕셔너리와 입력 받은 수가 같은 경우 {10,2} 
        a[t]+=1
    else:
        a[t]=1

    #최빈값 구할때 
for i, j in a.items():
    if max<j:
        max=j
        maxi=i

print(maxi)
'''
'''
a=dict()
#딕셔너리 2
maxh=0
max=0
for i in range(10):
    h=int(input())
    hap+=h
    if h in a:
        a[h]+=1
    else:
        a[h]=1
    if(max<a[h]):
        max=a[h]
        maxh=h
print(maxh)
'''
#리스트 방법 2
max=0
maxh=0
for i in range(10):
    h.append(int(input()))
    hap+=h[i]
for i in h:
    if max<h.count(i):
        max=h.count(i)
        maxh=i
print(maxh)





















