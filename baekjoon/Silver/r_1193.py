'''
[수학] 분수찾기 (실5)
1줄 1/1
2줄 1/2  2/1 => 12 흐름, 21 흐름
3줄 3/1 2/2 1/3  => 앞자리수 3 2 1 뒷자리: 1 2 3

'''

n = int(input())

cnt = 0 #현재까지 온 분수 갯수
line = 0 #현재 줄

# n번째 위치가 존재하는 '줄' 찾기
while n > cnt:
    line += 1 #1,2,3,4
    cnt += line #1 + 2 + 3 +...

# 현재 줄에서 n의 위치까지의 거리
dis = cnt - n

# 해당 줄이 짝수면: 1 2,  홀수면: 2 1임
if line % 2 == 0:
    front = line - dis #이렇게 할 수 있는 이유는 우리는 해당 줄 가장 끝에 있어서다.
    back = dis +1
else:
    front = dis + 1
    back = line - dis

print('%d/%d'%(front,back))




#시간초과
# n = int(input())
# cnt = 0 #현재 수
# check = False
#
# for i in range(1,n+1): # 1 1 21 2223
#     check = not check
#     for j in range(1,i+1):
#         cnt += 1
#         if cnt == n:
#             print('%d/%d'%(i,j))
#             break
#
#     for j in range(i + 1, 1, -1):
#         cnt += 1
#         if cnt == n:
#             print('%d/%d'%(j,i))
#             break
