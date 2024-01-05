# [덱] AC (골드5) _296ms, 41896kb
# 배열이 비어있는데 D를 사용한 경우에는 에러가 발생
# R : 뒤집기, D: 첫번째 수 버림
#  int로 변환해주는 것도 시간이 걸림.

# 깨달은 것 :
# 1
# R
# 0
# [] => R 결과 []
# 했을 경우에 에러가 나오면 안됨 [] 출력 해야함


from collections import deque

# import sys
# input = sys.stdin.readline
t_c = int(input())

for i in range(t_c):
    fc = input()  # 함수
    n = int(input())  # 배열의 갯수

    # 1. [1,2,3]을 리스트로 변환해 덱에 삽입
    arr_str = input().strip('[]') #
    if len(arr_str) != 0: # # 1,2,3
        # 덱에 담아주기 위해
        arr = [x for x in arr_str.split(',')] #[1,2,3]
        deq = deque(arr)
    else:
        # 배열에 아무것도 안 담겨 있는 상태에서 R을 했을 때에는, 함수가 돌아가야함.-> 전제에 문제가 생김
        # print("error")
        # continue
        deq = deque()

    rev_status = False  # 변환 여부
    for v in fc: # R D R D
        if v == 'R':
            rev_status = not rev_status  # 상태 바꿔줌
            # deq.reverse() -> 오래 거림
            # print("R: ", deq)

        # 맨 앞 빼는 연산
        elif v == 'D':
            if len(deq) == 0:
                print("error")
                break  # for in else:문으로 break시 else는 작동 x
            else:
                # 덱 : 양쪽에서 삽입 삭제가 됨
                if rev_status:  # 뒤집어진 상태 -> 현: 안뒤집어짐 그러니 반대로 빼줘야 함 #  2 3 4  -> 원본 4 3 2 1
                    deq.pop()
                else: #  2 3 4  (R연산이 x)
                    deq.popleft()

    # for _ in ~else:문 -> for문이 전부 정상 동작해야만 else문이 이어짐
    else:
        if rev_status:
            deq.reverse()
        print('[' + ','.join(map(str, deq)) + ']')