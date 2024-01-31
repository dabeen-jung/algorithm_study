# [백트래킹] n과 m(2)
# 오름차순으로 중복 x 수열
# ex) 3 1  -> 중복 없이 3개 중 1개씩 뽑을 때 출력
# import sys
# input = sys.stdin.readline
#
# n,m = map(int, input().split())
# res =[]
# arr = []
# check = [False] * (n+1)
#
# def f(num):
#     if num == m: #종료조건
#         arr.append(res)
#         print(' '.join(str,res))
#         return
#
#     for i in range(1,n+1): #1 ~ n+1 만큼
#         if check[i] == False:
#             check[i] = 1
#             res.append(i)
#             f(num+1)
#             check[i] = 0 #한 번 찍고 왔으니 False처리해줌
#
#
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
result = []

def f(start, depth): #
    if depth == m:
        print(' '.join(map(str, result)))
        return
    # 현재 시점에서 내가 갈 수 있는 영역에서 정함
    # (추리) 즉, 나보다 작은 수들은 이미 앞에서 썼을거라 생각함
    # (결과) f(i+1... 을 해서 +1 증가 시켜준 것 => 12, 21과 같은 중복 조합 방지
    for i in range(start, n+1):
        result.append(i)
        # i+1 : 본인은 제외하고 구한다.(중복x) / 깊이: ?번째에 들어가는 수
        f(i+1, depth+1)
        result.pop()

f(1, 0)

