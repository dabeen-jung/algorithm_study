'''
[수학] GCD 합 (실4)

'''

t_c = int(input())
arr = [list(map(int, input().split())) for _ in range(t_c)]

def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a

for t in arr:
    res = 0
    n = len(t)
    for i in range(1,n):
        for j in range(i+1, n):
            res += gcd(t[i],t[j])
    print(res)