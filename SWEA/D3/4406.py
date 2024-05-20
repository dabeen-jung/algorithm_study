'''
모음이 보이지 않는 사람

goal: a,e,i,o,u를 빼고 봐라
'''

for tc in range(1, int(input())+1):
    moem = ['a','e','i','o','u']
    ori = list(input())
    result = []
    for v in ori:
        if v not in moem:
            result.append(v)

    print(f'#{tc}', ''.join(map(str,result)))
