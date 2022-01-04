
lottos=list(map(int,input().split()))
wins=list(map(int,input().split()))

def solution(lottos, wins):
    answer = []
    t_0=lottos.count(0)
    cnt=0

    #.index(값) -> 없으면 에러남
    for i in (wins):
        if i in lottos:
            cnt+=1
    MAX=6-(cnt+t_0)+1
    MIN=6-cnt+1

    if(MIN==7):
        MIN-=1
    if(MAX==7):
        MAX-=1
    
    answer.append(MAX)
    answer.append(MIN)
    
    
    return answer
