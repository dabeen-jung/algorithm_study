#직사각형(백준 2527)
#goal: 주어지는 직사각형의 좌표들로 겹치는 부분에 대해 부호로 나타내라


#ar=[[int(i) for i in input().split()] for _ in range(4)]
#arr=[int(i) for i in input().split()]
#print(ar)

'''
for i in range(4):
    a,b,x,y,a_1,b_1,x_1,y_1 = map(int,input().split())
    #풀기 더 쉬운 것-> d,b,c,a

    
    if ((x < a_1 or a > x_1) or (y < b_1 or b > y_1) ): #'안 겹치는 경우 '
        print("d")
    elif ((x == a_1 and (y == b_1 or b == y_1)) or
          (x_1 == a and (y == b_1 or b == y_1)) ):  #'점'인경우
        print("c")
        
    elif ((b==y_1 and (a < a_1 < x or a_1 < a < x_1)) #X선분 겹칠때
          or (x==a_1 and (b <b_1<y_1 or b_1 < b < y_1 ))    #y선분 겹칠때
          or (b_1==y and (a<a_1<x or a_1< a < x_1) )#x선분 겹치는거())
          or (x_1==a and (b< y_1 <y or b<y<y_1) )#y선분일 경우(2,1)
          ):   
        print("b")

    else:   #사각형이 겹칠때 
        print("a")
        
#print(arr)
'''
for i in range(4):
    a,b,x,y,a_1,b_1,x_1,y_1 = map(int,input().split())

    if (a==x_1 and b==y_1) or (x==a_1 and b==y_1) or (a==x_1 and y==b_1) or(x==a_1 and y==b_1):
        print("c")
    elif (b==y_1) and (a_1<=a<=x_1 or a_1<=x<=x_1) or\
         (y==b_1) and(a_1<=a<=x_1 or a_1<=x<=x_1) or\
         (x==a_1) and (b_1<=b<=y_1 or b_1<=y<=y_1) or\
         (a==x_1) and (b_1<=b<=y_1 or b_1<=y<=y_1):
        print("b")
    elif x<a_1 or a>x_1 or y<b_1 or b>y_1:
        
        print("d")
    else:
        print("a")

