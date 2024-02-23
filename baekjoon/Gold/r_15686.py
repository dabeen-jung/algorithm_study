'''
[시뮬레이션] 치킨배달 (골 5)
r,c 는 1부터 시작

0 : 빈칸, 1: 집, 2: 치킨집 => 1-2

* 각 치킨거리 = |r1-r2| + |c1-c2|
* 즉, 도시 치킨거리 = '모든' 집의 각 치킨거리들의 '합'

goal:
최대 M개의 치킨집을 살리는 조건으로,
그 상태에서 골랐을 때 '도시의 치킨거리'가 최솟값을 출력
=> 최대 M개 치킨집이 있다 치고, 각 집 - 치킨집 거리들이 가장 작은 것들의 합의 최소값을 출력해라
'''



def f(a,b): # 치킨집 인덱스, 현재까지 선택한 치킨집 갯수
    global min_distance

    if a > len(chicken): #depth가 기존 치킨집 갯수를 뛰어 넘음
        return

    if b == m:
        distance_all = 0

        for x,y in house:
            distance = float('inf')
            # 2. 집 - 치킨집들의 거리를 일일히 비교
            for i in val:
                nx, ny = chicken[i]
                #치킨거리가 가장 짧았던 최소값 저장
                distance = min(distance, abs(nx-x) + abs(ny-y))
            #3. 짧았던 치킨거리들을 누적합 한 결과
            distance_all += distance

        #M개의 치킨집일 때 '모든 도시의 치킨집 거리'
        # => (각 치킨거리 최소 결과들의 모음)의의 최솟값'
        min_distance = min(min_distance, distance_all)
        # print("min_distance = ", min_distance)
        return

    val.append(a) #현재 치킨집 선택
    f(a+1, b+1) #if 현재 치킨집 선택 후, 다음 치킨집도 탐색
    val.pop() #현재 치킨집 선택을 취소
    f(a+1,b) #elif 현재 치킨집을 선택x , 다음 치킨집 탐색


#m = 남겨둘 치킨집 갯수(최대),
n,m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
chicken = []
house = []
val = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1: #집이다=> 저장
            house.append([i,j])
        elif arr[i][j] == 2: # 치킨 집이다 => 저장
            chicken.append([i,j])

# 최소값을 갱신해줄거임.(초기화)
min_distance = float('inf')
f(0,0)
print(min_distance)