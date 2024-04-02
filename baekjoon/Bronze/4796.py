'''
[수학] 캠핑
*캠핑장은 P일 중에 L일간만 쓸 수 있다.(아무리 더 사용하려 해도)

'''

check = True
cnt = 0
while check:
    cnt+=1
    result = 0
    L,P,V = map(int, input().split())

    if L == 0 and P ==0 and V ==0:
        break
    result += (L*(V//P))
    # L일보다 더 많이 나올 수도 있으니 확인
    result += min(L,V%P)
    print('Case %d: %d'%(cnt,result))