'''
#[백트래킹] 로또 (실2)

'''
import sys
input = sys.stdin.readline

tcase = []
# k = []
result = []

def f(S,start,depth):
    if depth == 6: #6까지만 만들 수 있다
        # print("nana",result)
        print(' '.join(map(str, result)))
        return

    for i in range(start,len(S)):
        result.append(S[i])
        f(S, i+1,depth+1)
        result.pop()

#1. 입력값 받기
while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break
    # k.append(a[0])
    tcase.append(a[1:]) # S의 1의 자리부터

for S in tcase:
    f(S,0,0) #배열, start, depth
    print()


