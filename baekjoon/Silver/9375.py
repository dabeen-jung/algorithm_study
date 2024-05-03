

tc = int(input())

for t in range(tc):
    n = int(input())
    kind = {}
    result = 1
    for i in range(n):
        name,k = input().split()
        # kind[k] = name

        if k in kind: #이 종류가 이미 존재?
            kind[k].append(name)
        else:
            kind[k] = [name] #append에는 문자열x, 리스트를 넣어야 함
    # print(kind)

    for kk in kind: #종류 딕셔너리에 key별로 꺼내기
        result *= (len(kind[kk])+1)
    print(result-1)

