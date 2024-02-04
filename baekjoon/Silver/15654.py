'''
[백트래킹] N과 M(5)
rule:
1. 주어진 배열에서 사전순으로 출력
2. m개 조합으로 출력
3. 11,22 (x)  / 17, 71(0)
'''

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
result = []
check = [False] * (n)

arr = list(map(int, input().rstrip().split()))
arr.sort()

def f(depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return

#1,7,8,9
    for i in range(n): #0~3 0
        if check[i] == False: #아직 안 씀
            check[i] = 1
            result.append(arr[i])
            f(depth+1)
            check[i]=0
            result.pop()

f(0)