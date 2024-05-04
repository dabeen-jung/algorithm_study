'''
[해쉬] 비밀번호 찾기 (실4)

list로 풀려고 했더니 시간 복잡도가 커질 수 있음 => 해시 테이블
* 해시테이블 구현하려면 '딕셔너리'를 사용

'''

n,m = map(int, input().split())
password = {}

for _ in range(n):
    site, pwd = input().split()
    password[site] = pwd

for _ in range(m):
    goal = input()
    print(password[goal])