'''
팔씨름

15번 팔씨름을 하여 8번 이상 이기는 사람이
->점심 값을 면제

S배열의 기준은 소영이 : ㅇ 승리, x 패배
goal: 소영이가 최종 점심값을 면제받을 가능성
15번째 판 후-> 적어도 8판이상 이겨야 함
'''

for t in range(1, int(input())+1):
    S = list(map(str,input()))
    k = len(S) #현재까지 진행한 판수
    win = 0 #5판 -> 15-8 7판 남 > (8-5)

    for v in S:
        if v == 'o':
            win += 1
    #15 중 4판함,3판 이김 -> 11판 중 8-3판 이기면 됨
    if  (15-k) - (8-win) >= 0:
        print('#%d YES'%(t))
    else:
        print('#%d NO' % (t))