#[큐(연결리스트)] - 요세푸스 (실버4)
#goal: 원에서 사람들이 제거되는 순서

from collections import deque

n,k = map(int,input().split())
deq = deque(range(1,n+1))

#결과를 기억
res = []

while deq: #큐가 소진 될 때까지
    for i in range(k-1):
        # 맨 앞의 자리를 돌아가며 k에 해당되지 않는지 확인하고,
        # 해당x면 뒤로 보냄
        deq.append(deq.popleft())
    res.append(deq.popleft())

#주의) 리스트으 ㅣ'문자열'을 연결할 때 join()을 쓰는거임
# 사이마다 빈칸이 추가적으로 들어감 => sep="" 처리
print("<",    ", ".join(map(str, res)), ">"  , sep="")

