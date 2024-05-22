# goal: 숫자가 겹칠 경우 한 개로 봐서 k개의 귤을 담되,
# 최소의 종류가 될 수 있도록
# from collections 를 이용하자!

from collections import Counter


def solution(k, tangerine):
    answer = 0
    arr = Counter(tangerine)
    print(arr)

    # {1:갯수,..} 이기에 [1] 인덱스
    arr2 = sorted(arr.items(), key=lambda x: x[1], reverse=True)

    for v in arr2:
        k -= v[1]
        answer += 1
        if k < 1:
            return answer

    return answer

k = int(input())
tangerine = list(map(int,input().split()))
print(solution(k,tangerine))