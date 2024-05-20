'''
영준이의 카드 카운팅
한덱 : 스페이드,다이아,하트,클로버 무늬 + 각각 A(1), 2~10, J(11), Q(12), K(13)
 =>이렇게 각 무늬별로 13개씩임 (총 52장)

goal: 기존 몇 장 외, 게임을 하기 위해 무늬 별로(S, D, H, C 순서로) 몇 장의 카드가 부족한지
+ 겹치는 카드가 있다? 오류도 출력
'''

for tc in range(1,int(input())+1):
    card = input()
    ori = [] #명령어 쪼개서 넣을 예정
    S,D,H,C = 13,13,13,13

    for i in range(0,len(card),3):
        if card[i:i+3] not in ori:
            if card[i] == 'S':
                S-=1
            elif card[i] == 'D':
                D-=1
            elif card[i] == 'H':
                H -= 1
            elif card[i] == 'C':
                C -= 1
            ori.append(card[i:i+3])
            # print(ori)
        else:
            print("#%d ERROR"%(tc))
            break
    else: #정상 작동시
        print("#%d %d %d %d %d" %(tc,S,D,H,C))


