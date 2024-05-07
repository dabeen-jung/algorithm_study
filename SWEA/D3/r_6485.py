'''
삼성시의 버스 노선

정류장 P개 - 노선은 N개
'''

for tc in range(1,int(input())+1):
    N = int(input()) #노선(가는 방법) 갯수
    notion = [0]*5001 #5000까지 만들고

    for i in range(N):
        a,b = map(int, input().split())
        for j in range(a,b+1):
            # 해당 정류장을 들리는 노선은 체크
            notion[j] += 1

    P = int(input()) #정류장(이 기준으로 셀거임)
    buslist = []
    for i in range(P):
        bus = int(input())
        buslist.append(notion[bus])

    print("#%d "%(tc),end='')
    for i in buslist:
        print(i,end=' ')
    print() #다음 커서를 위해 아래로 내려줌
