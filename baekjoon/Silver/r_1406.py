#에디터 (실버2) -연결리스트
# L : 커서 왼쪽 1칸(커서가 이미 맨 앞이면 무시)
# D : 오 ( 맨 뒤면 무시)
# B: 커서 왼쪽을 삭제 -> 오른쪽 x(맨앞이면 무시)
# P $ : $란ㄴ 문자를 왼쪽에 추가
import sys
from collections import deque
input = sys.stdin.readline

# 문자열을 덱으로 변환
#.strip()의 경우 '개행문자'까지 입력되어서 -> 앞뒤 공백제거함
str = deque(input().strip()) #왼쪽 덱
right = deque() #오른쪽 덱

n = int(input())

for i in range(n):
    ans = input().split()

    if ans[0] =='P':
        str.append(ans[1])

    elif ans[0] =='L':
        if str:
            #str(왼배열)의 끝을 삭제하며 이를 right(오른 배열)에 추가  str [ 1,2,3,]   right [1,5]
            right.appendleft(str.pop())

    elif ans[0] == 'D':
        if right:
            #right(오른배열)에서 맨 왼쪽 요소를 ㅇstr로 넘김
            str.append(right.popleft())
    else: #B일 경우
        if str:
            str.pop()

print(''.join(str + right))


# #? 왜 strip()을 넣었는가?
# #=>입력 받은 후 , 끝에 '\n'을 추가하기에
# str = input().strip()
# # print("초기값 str = " + str)
# cursor = 0
#
#
#
# n = int(input())
# idx = len(str)
#
# for i in range(n):
#     #매번 입력받는 값
#     ans = input().split()
#
#     if ans[0] =='P':
#         str = str[:idx] +ans[1] +  str[idx:]
#         # print("P인경우" + str )
#         idx+=1
#     elif ans[0] =='L':
#         #앞으로 한 칸
#         if idx == 0:
#             continue
#         else:
#             idx-=1
#     elif ans[0] == 'D':
#         #뒤로 한 칸
#         if idx == len(str):
#             continue
#         else:
#             idx+=1
#     else: #B일 경우
#         if idx == 0:
#             continue
#         str = str[:idx-1] + str[idx:]
#         # print("B인경우" + str )
#         idx-=1
#     # print("현재 인덱스 값 = %d"%(idx))
#
# print(str,end='')

