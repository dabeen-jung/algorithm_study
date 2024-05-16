'''
5일차 - GNS

goal: 작은 수부터 정렬하도록 출력
'''

for tc in range(1, int(input()) + 1):
    nums = {"ZRO": 0,
            "ONE": 0,
            "TWO": 0,
            "THR": 0,
            "FOR": 0,
            "FIV": 0,
            "SIX": 0,
            "SVN": 0,
            "EGT": 0,
            "NIN": 0}

    t,tlen = map(str,input().split())
    words = list(input().split())

    for v in words:
        nums[v]+=1
    print(f'#{tc}')


    for key,value in nums.items():
        if value == 0:
            continue
        else:
            print(' '.join([key]*value),end=' ')

    print()

#개쩌는 분 코드
# T = int(input())
#
# # 정렬을 위한 딕셔너리
# num_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
#
# for test_case in range(1, T + 1):
#     num, N = input().split()
#     # 문자열을 리스트로 받아옴
#     num_list = list(input().split())
#
#     # 리스트를 딕셔너리의 value를 기준으로 정렬 후 출력
#     num_list.sort(key=lambda x: num_dict[x])
#     print(num)
#     print(' '.join(num_list))