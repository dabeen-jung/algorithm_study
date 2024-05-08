'''
원 안의 점
'''

for tc in range(1,int(input())+1):
    n = int(input())
    result = 0
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            if i**2 + j**2 <= n**2:
                result += 1
    print("#%d %d" % (tc, result))