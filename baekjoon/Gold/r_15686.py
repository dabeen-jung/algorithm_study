'''
[시뮬레이션] 치킨배달 (골 5)
r,c 는 1부터 시작

0 : 빈칸, 1: 집, 2: 치킨집

* 각 치킨거리 = |r1-r2| + |c1-c2|
*  도시 치킨거리 = '모든' 집의 각 치킨거리들의 '합'

? 수익을 가장 많이 냄 =
goal:
1. 수익을 많이낼 수 있는 치킨집 갯수를 알려줄거
-> '도시의 치킨거리'의 최솟값
'''



def close(a,b): # 요구사항인 M개 만큼 치킨집을 폐업해보자
    global min_distance

    if a > len(chicken):
        return

    if b == m:
        distance_all = 0

        for x,y in house:
            distance = float('inf')
            for i in val:
                nx, ny = chicken[i]
                distance = min(distance, abs(nx-x) + abs(ny-y))
            distance_all += distance
        min_distance = min(min_distance, distance_all)
        return

    val.append(a)
    close(a+1, b+1)
    val.pop()
    close(a+1,b)


#m = 남겨둘 치킨집 갯수(최대),
n,m = map(int, input().split())
arr = list(map(int,input().split()))
chicken = []
house = []
val = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i,j])
        elif arr[i][j] == 2:
            chicken.append([i,j])

min_distance = float('inf')
close(0,0)
print(min_distance)