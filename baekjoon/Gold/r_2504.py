#[스텍] 괄호의 값 (골드5)
# 조건: 괄호 안에 있는거면 무조건 곱해줌
#분배법칙을 생각 A(B+C) => A*B + A*C와 같음

#왜 못풀었을까? 문제에 대한 접근을 잘 못함


arr = input()
stack = []
res = 0 # 총 결과값
tmp = 1 # 중간 누적값 => 곱을해줘야 해서 기본값 1

for i in range(len(arr)): # (
    v = arr[i]

    if v == '(':  # tmp = 2*2 = 4
        tmp *= 2   # ( () [[]] ) => 2*1 =2
        stack.append(v) # stack  =  [ '(', '('    ]
    elif v == '[':
        tmp *= 3
        stack.append(v)

    #닫히는 애들
    elif v == ')':    #()  stack= [  '('  ]
        if not stack or stack[-1] == '[':
            res = 0
            break
        if arr[i - 1] == '(':
            res += tmp   #tmp = 4 res+=4    #  stack =['('] =>2* ?   => 2* (2 + ?) = 2*2   + 2*?
        # (다시 나눠서)원 상태로 돌려줌
        # 즉 (곱셈을 해줬으니까(열린괄호 때마다)) 나눠서 초기화 해줌
        tmp //= 2   #tmp = 4  -> tmp =2 *
        stack.pop()

    else: #닫는 괄호 ), ]
        if not stack or stack[-1] == '(':
            res = 0
            break
        # 실제 arr 배열에서 []이 아니라 [[]] 중 끝에 해당됨
        # 즉 직전 배열이 맞닿는 [] 이런 괄호가 x => 더해주지 x
        if arr[i - 1] == '[': # stack=[ '(', '[', '(']
            res += tmp
        tmp //= 3
        stack.pop()

if stack:# stack = ['(']
    res = 0
print(res)