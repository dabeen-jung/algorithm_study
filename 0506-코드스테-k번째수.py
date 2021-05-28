
def solution(n, lost, reserve):
    answer = 0
    cnt=0
    
    s_reserve=set(reserve)-set(lost)
    
    
    print(s_reserve)
    print(reserve)
           
    return answer



print(solution(5,[2,4],[2,3,5]))
