#제로(실버4) (스택)
#잘못된 수 일 때 0을 외침 -> 최근 적은 수 삭제


k = int(input())
arr=[]
for i in range(k):
    ans = int(input())
    if ans == 0:
        arr.pop()
    else:
        arr.append(ans)

print(sum(arr))