'''
[정렬] 시리얼 번호 (실3)
AB 인경우,

'''

import sys
input = sys.stdin.readline

N = int(input())
#arr = [input().rstrip().split() => list 로 반환되어서 2중 list가 됨
# arr = [input().rstrip() .... ] => 문자열로 반환됨 list 하나가 끝임 
arr = [input().rstrip().split() for _ in range(N)]
# print(arr)

def digist_s(x): # '1A2CF' 가 올 때
    return sum(int(c) for c in x if c.isdigit())

# 1. len(x) 문자열 길이순
# 2. 1번에서 문자열 길이가 같다면, 숫자들의 합 비교(함수를 수행)
# 3. 사전순 (숫자가 먼저, 그다음 영어)
# ex) 얘는 x = ['ABCD'] , 즉 arr 배열 한 단위의 길이 => 1임
# sorted_list = sorted(arr, key=lambda x: (len(x) ))

arr.sort(key = lambda x : (len(x[0]),digist_s(x[0]),x[0]))

for v in (arr):
    print(''.join(v))