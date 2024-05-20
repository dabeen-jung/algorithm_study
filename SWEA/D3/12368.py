'''
24시간
자정(0시)에서부터 지금까지 흐른 시간을 기준으로 시각을 표기
오후 8시 -> 20시

goal: 자정에서~A시간이 지남 + 여기서 B시간이 더 지난다? 몇 시인가
'''

for t in range(1, int(input())+1):
    A,B = map(int, input().split())
    S = A+B
    if S >= 24:
        print(f'#{t} {S%24}')
    else:
        print(f'#{t} {S}')