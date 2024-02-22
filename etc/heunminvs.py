


num = int(input())
arr = [1,2,3]
victory = False

def f (turn, n):
    global victory

    if victory:
        return

    if turn % 2 == 1 and n==4:
        return

    #종료조건
    if turn % 2 == 0 and n == 4:
            victory= True
            return

    for i in arr:
        if n-i >= 1:
            f(turn+1 ,n-i)

f(0,num)
if victory == True:
    print("true")
else:
    print("false")