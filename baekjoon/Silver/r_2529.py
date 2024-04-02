'''
[백트래킹] 부등호 (실1)

goal:
1. 부등호 기호 앞 뒤에 서로 다른 '한자릿 수'를 넣었을 때 부등호 관계가 맞게
2. 이어지는 최대 정수, 최소 정수를 출력 ex) 0123...
'''

import sys
input = sys.stdin.readline

k = int(input())
inequality = list(map(str,input().rstrip().split()))
visited = [0] * 10
MIN = ""
MAX = ""


def dfs(depth,num):
    global MIN, MAX

    # print(num,depth)
    #종료조건
    if depth == k+1:
        # 제일 처음 온 수가 최솟값일 수밖에 없고, 마지막으로 오는게 최댓값임
        if len(MIN) == 0:
            MIN = num
        else:
            MAX = num
        return

    for i in range(10): #숫자(k번 거칠거임) A < B ....  2 < 3
        if not visited[i]:
            if depth == 0 or (inequality[depth-1] == '<' and int(num[-1]) < (i)) or (inequality[depth-1] == '>' and int(num[-1])> i):
                visited[i] = True
                dfs(depth + 1, num + str(i))
                visited[i] =False


dfs(0, "")
print(MAX)
print(MIN)