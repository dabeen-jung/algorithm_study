#[재귀] 별찍기-10 (골5)

import sys
input = sys.stdin.readline

# n = (3,7,27...)
n = int(input())
arr = [[' ' for _ in range(n)] for _ in range(n)]


def rep(l):

    div = l//3
    if l == 3:
        arr[1] = ['*', ' ', '*']
        # *** 구간임
        #
        # ***
        arr[0][:3] = arr[2][:3] = ['*'] * 3
        return

    rep(div)

    for i in range(0,l, div):
        for j in range(0, l, div):
            if i != div or j != div:
                for k in range(div):
                    arr[i+k][j: j+div] = arr[k][:div]

rep(n)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end='')
    print()

