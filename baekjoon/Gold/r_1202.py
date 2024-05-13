'''
[이진검색트리] 보석도둑 (골2)
보석은 N개, 각 보석(M, V가격)
가방 k 개, 각 담을 수 있는 최대 무게 Ci => 가방에 1개 보석만

1.무게가 작은 가방 - 들어갈 수 있는 보석 중 비싼 보석

goal 훔칠 수 있는 보석의 최대가격
'''
import sys
import heapq

input = sys.stdin.readline
n,k = map(int,input().split()) #가방,보석 갯수

#보석 정보 (무게,가격) => 가격,무게
gem = [list(map(int,input().split())) for _ in range(n)]
# print(gem)
#가방 정보 (최대무게)
bags = [int(input()) for _ in range(k)]
maxQ = [] #최대힙
money = 0

bags.sort() #가벼운 순 O(n)
gem.sort()


#목표 : 무조건 가격부터 봄(들 수 있는 무게면 됨)
for bag in bags:
    while gem and bag >= gem[0][0]: #보석무게가 가방보다 가볍다
        heapq.heappush(maxQ, -gem[0][1]) #가격 삽입
        # 보석에서 우선 빼준 후 해당 보석은 최대힙에서 관리
        heapq.heappop(gem)
        # print(gem)
    # 가벼운 가방 무게에 맞고, 최대 가격으로 들어갈 수 있는 보석
    if maxQ: #힙에 값이 있어야
        money += (-heapq.heappop(maxQ))

print(money)