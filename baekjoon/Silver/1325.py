'''
[그래프] 효율적인 해킹
*  한 번의 해킹으로 ->
'여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터'를 해킹하려고 한다.

* 신뢰관계
신뢰하는 관계, 신뢰x 관계
* A->B =>> 신뢰 B해킹하면 이어지는 A도 해킹함

goal: 한 번에, '가장 많은 컴퓨터를 해킹할 수' 있는 컴퓨터의 번호
'''


#메모리초과라 pypy로 냄
# 그래도 메모리 초과가 나서 int타입을 -> bool 타입으로 바꾸라함

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True
    cnt =1 #시작노드부터 1

    while q:
        x = q.popleft() #현 시작 노드

        for v in graph[x]:
            if not visited[v]:
                visited[v] = True #방문함
                q.append(v)
                cnt += 1
    return cnt


#1. 값들 선언
n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    #a가 b를 신뢰함
    a,b = map(int,input().split())
    #신뢰를 많이 받는 애들한테 : 신뢰하는 애들이 붙음
    #b 를 해킹하면 A도 해킹됨
    graph[b].append(a)


res = []
# 2. 가장 거치는 정점이 많은 애를 기록 및 해당 정점번호 출력
for i in range(1,n+1):
    res.append(bfs(i)) #cnt 각각 저장

#3. 최대 노드 (값이 비슷하면 둘다 출력)
MAX = max(res)
for i in range(n):
    if MAX == res[i]:
        print(i+1 , end= ' ')
