#개미(백준 10158번)
w,h=map(int,input().split())
a,b=map(int,input().split())
t=int(input())



'''
while(tt<=t):   #w인 경우 
    if(a==0):
        w=

    if(a==w):

while(tt<=t):   #h인 경
'''
result_x = (t+a) % (w*2)
if(result_x > w):   
    result_x=w-(result_x % w)

result_y=(t+b)%(h*2)
if(result_y > h):   
    result_y = h - (result_y % h)

print(result_x, result_y)
