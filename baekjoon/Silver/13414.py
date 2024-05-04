'''
[해쉬] 수강신청(실3)
1.활성화 된 후, 수강신청 버튼을 조금이라도 빨리 누른 학생이 대기목록에 먼저 들어감
2.이미 대기열에 있는데, 중복되어 있다> 앞에꺼 지움 & 뒤에는 남김
3. 비활성이 되면, 대기목록 순별로 완료됨, 꽉차면 나머지는 무시하고 종료

goal: 성공한 학번만 출력해라
'''


import sys
input = sys.stdin.readline

#수강가능인원, 클릭한 대기목록 길이
K,L = map(int, input().split())
click = {}

for i in range(L):
    a = input().rstrip()#학번 시작이 0부터일 수도 있음
    click[a] = i
# print(click)
#(키, 값)
arr = sorted(click.items(), key = lambda x:x[1])

#수강신청 인원이 정원보다 적을 수도 있음
cnt = 0
for v in arr:
    if cnt == K:
        break
    cnt+=1
    print(v[0])


