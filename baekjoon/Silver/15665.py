'''
[백트래킹] N과 M(11) (실2)
1. 중복 x
2. 같은 수가 오는건 ㄱㅊ 11 77
3. 사전순으로

'''


n,m = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []
prev = 0

def f(depth):
    prev = 0
    #종료
    if depth == m:
        print(' '.join(map(str, result)))
        return

    for i in range(n):
        # 처리가 다 끝난 값이 또 나왔는지 확인용
        if prev != arr[i]: #직전 나온 값과 같은가? ex 19 후에, 또 19?
            # print("prev ",prev, arr[i])
            result.append(arr[i])
            # print(result)
            prev = arr[i]

            f(depth + 1)
            result.pop()

f(0)
