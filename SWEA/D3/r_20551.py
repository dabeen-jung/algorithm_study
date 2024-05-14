'''
[D3] 증가하는 사탕 수열
1상자:a  2상자:b  3상자:c

-> a<b<c , 모든 사탕은 기본 1개 이상 담겨있다

goal: 두 조건을 만족하도록 , 최소 몇 개 사탕을 먹어야 하나?
'''
t = int(input())
for tc in range(1, t + 1):
    cnt = 0
    candies = []
    candies += map(int, input().split())

    if candies[2] < 3 or candies[1] < 2:
        print(f"#{tc} -1")
        continue

    if candies[2] <= candies[1]:
        cnt += candies[1] - candies[2] + 1
        candies[1] = candies[2] - 1

    if candies[1] - candies[0] <= 0:
        cnt += candies[0] - candies[1] + 1

    print(f"#{tc} {cnt}")

#[시간만료]
# for t in range(1,int(input())+1):
#     candys = list(map(int,input().split()))
#     eat = 0
#
#     while candys[1] >= candys[2]: # 2 7 5
#         candys[1]-=1
#         eat += 1
#
#     while candys[0] >= candys[1]:
#         candys[1]-=1
#         eat += 1
#
#     if candys[0] == 0 or candys[1] == 0 or candys[2] == 0:
#         print(f'#{t} {-1}')
#     else:
#         print(f'#{t} {eat}')

