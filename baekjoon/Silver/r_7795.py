'''
[정렬] 먹을 것인가 ㅁ거힐 것인가
 A= {8, 1, 7, 3, 1} / B={3, 6, 1}
=>8-3, 8-6, 8-1, 7-3, 7-6, 7-1, 3-1

goal: 각 테스트케이스마다, A>B '쌍의 갯수'를 출력해라
'''

import sys
input = sys.stdin.readline

t_c = int(input())

# [시간초과] On(N*M) .
# def f_cnt(A,B):
#     cnt = 0
#     for a in A:
#         for b in B:
#             if a > b:
#                 cnt+=1
#     return cnt

def f_cnt(A,B):
    cnt,idx = 0,0
    A.sort()
    B.sort()

    for a in A:
        # idx가 증가하며, 그 전의 B의 원소는 무조건 통과됨
        # 이유: (오름차순 정렬 땜에)
        # 그래서 셋다 치고 idx가 증가된 상태로 '카운트' 하는거임
        while idx < len(B) and a > B[idx] :
            idx += 1
        cnt += idx
    return cnt

for i in range(t_c):
    N,M = map(int, input().rstrip().split())
    A = list(map(int, input().rstrip().split()))
    B = list(map(int, input().rstrip().split()))

    print(f_cnt(A,B)) #함수호출