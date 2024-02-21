'''
[구현] 누울 자리를 찾아라 (실5)

goal: 2개이상 빈칸(.)이 가로 몇개인지/ 세로 몇 개인지

row
세야할 때,
1. '.' : row+=1
2. 'X' 만나면, row = 0
    행이 끝나면서 row>=2 , row = 0



'''


n = int(input())
arr = [list(map(str, input())) for _ in range(n)]

print(arr)

row_cnt = 0 #가로 갯수
col_cnt = 0 #세로 갯수
row = 0
col = 0

for i in range(n):
    row = 0
    for j in range(n):
        if arr[i][j] == '.':
            row+=1

        elif arr[i][j] == 'X':
            if row >= 2: #누울 수 있어
                row_cnt +=1
            row = 0

        if j == n-1: #마지막 행이 끝났을 때
            if row >=2: #누울 수 있으면
                row_cnt +=1


        if arr[j][i] == '.':
            col+=1

        elif arr[j][i] == 'X':
            if col >= 2: #누울 수 있어
                print("세로 세짐 %d %d %d"%(j,i,col))
                col_cnt +=1
                col = 0
            else:
                col = 0
            print("col 리셋", col)

        if i == n-1:
            if col >=2:
                col_cnt +=1
                col = 0
            else:
                col = 0
print(row_cnt, col_cnt)
