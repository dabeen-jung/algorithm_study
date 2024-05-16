'''
원재의 메모리 복구하기

초기화(0000..) ->원래값
goal: 초기화에서 원래상태로 바뀌기 위해 최소 몇 번을 고쳐야하나?

* 앞의 자리부터 1이 나온다? ->0(반대)이 나오는 경우 세기
* 앞의 자리가 0이 나옴 -> 1(반대 되는) 경우가 나오면 세기
'''

for tc in range(1, int(input())+1):
    nums = input()

    cnt = 0
    before = 0
    for v in (nums):
        if int(v) != before:
            cnt+=1
            # print('')
            before = int(v) #바꿔줌 0->1로/ 1->0으로

    print(f'#{tc} {cnt}')