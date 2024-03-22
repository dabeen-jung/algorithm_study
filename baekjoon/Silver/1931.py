'''
[그리디] 회의실 배정 (실1)
goal:  회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수
+) 끝남과 동시에 다른 회의를 시작(ㅇ)
'''
import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key = lambda x : (x[1],x[0]))

cnt = 1 #갯수
end = arr[0][1]

for i in range(1,n):
    if end <= arr[i][0]:
        end = arr[i][1]
        cnt+=1

print(cnt)

