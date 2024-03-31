'''
[수학] 팩토리얼 0의 개수

10! = 1*2*3*4*5*6*7*8*9*10
'''

n = int(input())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

arr = str(factorial(n))
cnt = 0

for i in range(len(arr)-1, -1, -1):
    if arr[i] == '0':
        cnt += 1
    else:
        break
print(cnt)