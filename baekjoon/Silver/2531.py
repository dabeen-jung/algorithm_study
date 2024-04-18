'''
[투포인터] 회전초밥 (실1)

* 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격
*ㄴ> 위의 행사에 참가시, 쿠폰(초밥 종류번호)의 => 해당 초밥 하나를 무료로 제공 -> 없다? 새로 만듦

\goal: 손님이 먹을 수 있는 초밥 가짓수의 (최대)는?
'''

#접시수, 초밥 가짓수, 연속접시수, 쿠폰번호
N,d,k,c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

sushi += sushi[:k - 1]  # 회전 초밥이므로, 마지막에서 시작하여 앞 접시들을 선택할 수 있게 리스트를 확장
print(sushi)
kind = 0  # 먹을 수 있는 초밥 가짓수
max_kind = 0  # 최대 초밥 가짓수

from collections import defaultdict

counter = defaultdict(int)

for i in range(k):  # 처음 k개의 초밥을 선택
    if counter[sushi[i]] == 0:
        kind += 1
    counter[sushi[i]] += 1
    print(counter)

if c not in sushi[:k]:
    max_kind = kind + 1
else:
    max_kind = kind

for i in range(k, len(sushi)):
    left = i - k  # 범위에서 제외될 초밥
    right = i  # 범위에 포함될 새로운 초밥

    counter[sushi[left]] -= 1
    if counter[sushi[left]] == 0:
        kind -= 1

    if counter[sushi[right]] == 0:
        kind += 1
    counter[sushi[right]] += 1

    if c not in sushi[left + 1:right + 1]:
        max_kind = max(max_kind, kind + 1)
    else:
        max_kind = max(max_kind, kind)

print(max_kind)