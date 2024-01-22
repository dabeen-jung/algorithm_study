# [재귀, 분할정복] Z (실1)
# 오류 : 재귀 길이 때문에 오류
import sys
input = sys.stdin.readline

n,r,c = map(int, input().split())


def rep(n, x, y):
    if n == 2:
        # x==r이고, y==c가 아니면 None값이 나옴 (X)
        #return (x == r) * 2 + (y == c)
        if x==r and y == c:
            return 0
        if x == r and y+1 == c:
            return 1
        if x+1 == r and y == c:
            return 2
        if x+1 == r and y+1 == c:
            return 3

    n //= 2 #한 변의 길이(가로,세로 등)

    if x <= r < x+n and y <= c < y+n:  # Z의 1사분면
        return rep(n, x, y)

    if x <= r < x+n and y+n <= c:  # Z의 2사분면
        return n*n*1 + rep(n, x, y+n)

    if x+n <= r and y <= c < y+n:  # Z의 3사분면
        return n*n*2 + rep(n, x+n, y)

    if x+n <= r and y+n <= c:  # Z의 4사분면
        return n*n*3 + rep(n, x+n, y+n)

print(rep(2**n, 0, 0))


# graph = [[0]*(2**n) for _ in range(2**n)]
#
# print(graph)
#
# cnt = 0
#
# dx = [0,0,1,1] #z형태로 이동
# dy = [0,1,0,1]
#
# def rep(x,y):
#     # 2**(n-1) 별로 재귀 돌림?
#     global cnt
#     cnt+=1
#
#
#     for i in range((2**n)//2):
#         for j in range(4):
#             x = x + dx[j]
#             y = y + dy[j]
#
#             if x == r and y == c:
#                 return cnt
#             cnt+=1
#
#         rep(x,y)
#
# print(rep(0,0))