'''
8일차 암호문3
암호문 덩어리들이 총 N개

* I x,y,s : x번째 담에, y개 암호를 넣을거임 (s들로)
* D x,y : x번째 담, y개 암호문을 삭제
*A y,s : 맨 뒤에 y개 암호문 붙임, (s를 넣겟다)

goal: 처음 10개 암호문을 출력

왜 어려웠나? 리스트 기초 함수중 삽입, index,find 등의 기능을
제대로 알고 쓰지 못했다.
'''


for tc in range(1, 11):
    N = int(input()) #암호문 갯수
    secret = list(map(int,input().split())) #암호문 덩어리들
    k = int(input())#명령어 갯수
    li = input().split()

    i = 0
    for idx in range(len(li)):
        if li[idx] == 'I':
            #I x,y,s    x번째 담에, y개 암호를 넣을거임 (s들로)
            x = int(li[idx + 1])
            y = int(li[idx + 2]) #y개
            for i in range(y):
                secret.insert(x+i, li[idx + i + 3])
            # plus = list(map(int,li[i+3 : i+3+y]))
            # secret[x+1:x+1] = plus #저 리스트를 x다음에 넣어줘
        elif li[i] == 'D':
            #D x,y : x번째 담, y개 암호문을 삭제
            x = int(li[i+1]) #x위치
            y = int(li[i+1]) #y개 삭제하자
            del secret[x:x+y]

        elif li[i] == 'A':
            #A y,s : 맨 뒤에 y개 암호문 붙임, (s를 넣겟다)
            y = int(li[i + 1])  # y개
            for i in range(y):
                secret.append(li[idx + 2 + i])
            # plus = list(map(int, li[i+2: i+2+y] ))
            # secret.extend(plus)
            # i += 2+y


    print(f'#{tc}', ' '.join(map(str,secret[:10])))