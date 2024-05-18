'''
회의실 배정
회의의 시작시간과 끝나는 시간이 같을 수도 있다. (끝나자마자 시작하기)
goal:각 회의가 겹치지 x,회의실을 사용할 수 있는 회의의 최대 개수
'''

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
#회의가 가장 빨리 끝나는 순으로
arr.sort(key = lambda x : (x[1],x[0]))

# print(arr)
MAX = 0 #끝난시간
cnt = 0
for i in range(N):
    if arr[i][0] >=MAX: #시작 시간과 비슷
        MAX = arr[i][1] #끝나는 시간(한계)기준으로 재설정
        cnt += 1

print(cnt)