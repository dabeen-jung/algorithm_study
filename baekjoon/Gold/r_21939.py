'''
[이진검색트리] 문제 추천시스템 Version1 (골4)

recommend x
if x ==1: 가장 어려운 문제 번호 출력(여러개? 번호가 큰 것을 출력)
elif x== -1: 가장 쉬운 문제 번호(여러개 -> 번호가 작은것)

add P L : L난이도 P번호 문제를 추가
solved P : P번호 문제를 제거

https://windy7271.tistory.com/entry/Python%F0%9F%A5%874%EB%B0%B1%EC%A4%80%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-21939%EB%B2%88-%EB%AC%B8%EC%A0%9C-%EC%B6%94%EC%B2%9C-%EC%8B%9C%EC%8A%A4%ED%85%9C-Version1
목표 : recommend 명령어가 나올때만 추천 번호 출력
질문 : 왜 최소힙,최대힙을 양쪽 둘 다에 적용하지 않는 것인가?
recommend n 의 숫자와 solved 문제번호가 겹친 경우에 그 힙에만 적용이 되나?
'''

import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

minQ = []
maxQ = []
N = int(input())
deleted = defaultdict(int)

for i in range(N):
    P,L = map(int, input().split())
    heapq.heappush(minQ,(L,P)) #난이도 기준 정렬,번호기준
    heapq.heappush(maxQ, (-L,-P))


M = int(input())
for i in range(M):
    line = input().split()

    if line[0] == 'add':
        L = int(line[2])
        P = int(line[1])
        heapq.heappush(minQ,(L,P))
        heapq.heappush(maxQ,(-L,-P))


    # 우선순위큐(최소힙,최대힙)에서 P번 문제 제거
    elif line[0] == 'solved':
        deleted[int(line[1])] += 1 #해당 문제번호 삭제처리
        # print("삭제한 번호 리스트 값",deleted[int(line[1])])

    elif line[0] == 'recommend':

        if int(line[1]) == 1: #난이도 높은 문제
            # 삭제리스트[문제번호]에서 현 최대큐 우선순위값이
            # 이미 solved에서 삭제처리 한 애임 => 여기서도 삭제해주자
            while deleted[abs(maxQ[0][1])] != 0:
                #굳이 빼주는 이유는
                # -> 또 add (삭제했던)문제번호, 난이도로 들어올 수 있기에
                deleted[abs(maxQ[0][1])] -= 1 #0
                heapq.heappop(maxQ) #해당 값은 큐에서 정말 삭제
            print(-maxQ[0][1])
        else:
            while deleted[minQ[0][1]] != 0:
                deleted[minQ[0][1]] -= 1
                heapq.heappop(minQ)
            print(minQ[0][1])

        # print("minQ",minQ)
        # print("maxQ",maxQ)
