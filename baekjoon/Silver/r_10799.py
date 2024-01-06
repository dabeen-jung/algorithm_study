#쇠 막대기

arr = input()

stack = []
res = 0

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append('(')

    else: #')
        if arr[i-1] == '(' : #레이저임
            stack.pop() #레이저
            res += len(stack) #지금까지 남아있는 막대갯수 더해주기

        else: # ')'로 막대의 끝임
            stack.pop()
            res+=1 #막대의 오른쪽 부분을 세주면서 끝냄
print(res)



