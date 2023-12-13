#빙고_(백준 2578)_e-3
#goal: 빙고(3줄 이상)를 외칠 때, 사회자가 몇 번째 수를 불렀는가?  

dice=[[int(i) for i in input().split()] for j in range(5)]
ar=[[int(i) for i in input().split()] for j in range(5)]

t=0 #빙고 수

for k in ar:
    #매번 t를 초기화해서 총 빙고 3번이 나올때까지 빙고에 0을 누적
    for i in range(5):
        for j in range(5):
            if k==arr[i][j]:
                arr[i][j]=0

            #경우의 수를 다 여기에 체크해주            
            if (dice[0][0]== 0 and dice[1][1]==):
