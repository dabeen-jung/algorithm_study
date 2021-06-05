#1714 숫자 거꾸로 출력하기
n=input()

stack=[]

for i in n:
    stack.append(i)

for i in range(len(stack)):
    print(stack.pop(),end='')

