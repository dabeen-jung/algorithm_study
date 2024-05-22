'''
[우선순위 큐] 파일 합치기3

1.두 개의 파일을 합침 -> 하나의 임시파일을 만들고,
2.이 임시파일 or 원래의 파일을 계속 두 개씩 합쳐서 파일을 합쳐나가고,
=>최종적으로는 하나의 파일로 합친다.
비용 = 2파일 크기 합

goal: 파일들을 최종 1개까지 만드는데 비용(최소) 구하기

'''
import heapq
import sys
input = sys.stdin.readline


for t in range(int(input())):
    k = int(input())
    arr = list(map(int,input().split()))

    heapq.heapify(arr) #리스트를 -> 최소힙으로 변환
    result = 0
    #갯수가 마지막 1개 남을 때까지
    while len(arr) > 1:
        #현재 우선순위 큐에서 가장 작은 것끼리
        v1 = heapq.heappop(arr)
        v2 = heapq.heappop(arr)

        hap = v1+v2
        result += hap
        heapq.heappush(arr,hap) #이후에 더해야 할 값 중 한 개임

    print(result)