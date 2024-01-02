#[덱] 회전하는 큐 (실버3)
# 첫번째 원소 뺌
# 맨 앞->맨뒤로 이동시킴 231
# 맨 뒤 -> 맨 앞으로 이동 3123
# 궁금점: //2와 /2의 경우 소숫점 여부의 차이임
#=> 어차피 if로 작은경우 외에 동일하거나 더 큰 경우에도 cnt+=1 해주는데
#왜 14 , 16 차이가 날까

from collections import deque
import sys
input = sys.stdin.readline


#큐의크기, 뽑으려는 갯수
n, m = map(int,input().split())
# 뽑아내려고 하는 위치(가장 처음 큐에서의 위치)
idxs = list(map(int, input().split()))
deq = deque([i for i in range(1, n+1)])

cnt = 0

for idx in idxs: #뽑아내려는 수 위치를 꺼내서 비교
    while 1:
        if deq[0] == idx: # 맨앞 원소 == 현 idx 같다
            deq.popleft() #1번 연산 수행 (count x)
            break
        else:
            #덱에서 찾고자 하는 인덱스 위치가 , 절반보다 훨씬 앞쪽에 있다.(인덱스가 작다)
            if deq.index(idx) < len(deq)/2 : # 소숫점도 나와야 함 (동일할 경우도 있음)
                while deq[0] != idx: # 맨 앞이 같아질때까지 반복
                    # 2번 연산 (해당 원소가 앞으로 가게 밀어줌)
                    deq.append(deq.popleft())
                    cnt +=1

            else: #(인덱스가 비교적 절반보다 뒤에 위치)
                while deq[0] != idx:
                    deq.appendleft(deq.pop()) # 3번 연산
                    cnt +=1

print(cnt)


