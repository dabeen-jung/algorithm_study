'''
최대 성적표 만들기

goal: k개 과목을 선택해서 성적표 총점이 가장 최대로 만들어라
'''

for tc in range(1, int(input())+1):
    #총 과목, k과목
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))

    arr.sort(reverse=True)
    print(f'#{tc} {sum(arr[:k])}')