'''
[D3] 햄버거 다이어트
1. 재료를 자르지 x
2. 재료는 1번만 사용
3. 점수는 맛점수로

왜? dfs 접근 생각을 못하고 우선순위큐로 접근햇음
goal: 가장 맛에 대한 점수가 높고, 정해진 칼로리를 넘지 않는 햄버거
'''

def dfs(start, score, kcal):
    global max_score

    if kcal > L:
        return
    if kcal <= L:
        if score > max_score:
            max_score = score
    #재귀
    for i in range(start,N):
        dfs(i+1, score + ingre[i][0], kcal + ingre[i][1])


for tc in range(1, int(input())+1):
    #재료 수, 제한 칼로리
    N,L = map(int,input().split())

    #재료에 따른 맛 평가 (점수,칼로리)
    ingre = [list(map(int,input().split())) for _ in range(N)]

    max_score = 0
    dfs(0,0,0)
    print(f'#{tc} {max_score}')