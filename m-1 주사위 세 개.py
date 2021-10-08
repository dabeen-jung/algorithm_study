#주사위 세 개
'''
중복된 애를 굳이 찾고 싶다면...
a.count(a[0]) -> 0번 인덱스의 값과 같은애가 나오면,,?
[1,2,3] -> 1개
[1,1,2] -> 2개 일거,,

하지만 [1,3,3] -> 1개 일터이니 한 번 더 확인을 하는 과정이 필요함,,
a.count(a[1]), a.count(a[2]) 이렇게

위나 아래나 비슷비슷하니
다른 방법의 존재만 이해하고 넘어가자
'''
a,b,c=map(int,input().split())
hap=0

if(a==b and a==c ):
    hap=10000+(a*1000)
    
elif(a==b and a!=c):
    hap=1000+(a*100)
elif(b==c and a!=b):
    hap=1000+(b*100)
elif(c==a and b!=a):
    hap=1000 + (c*100)

else:
    hap=100*max(a,b,c)

print(hap)
