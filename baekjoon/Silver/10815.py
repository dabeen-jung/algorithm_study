'''
[dp] 숫자 카드 (실5)
N(1 ≤ N ≤ 500,000)
값들은  -10,000,000보다 크거나 같고, 10,000,000보
'''


# list에서 in 수행시 모든 요소를 처음부터 검사하면서 찾는 원소가 있는지 확인,
# set은 해시로 구현되어 있어 x in set 이 x in list보다 일반적으로 더 빨리 동작하게 된다.
n = int(input())
arr = set(map(int, input().split()))

m = int(input())
diff = list(map(int, input().split()))

for v in diff:
    if v in arr:
        print("1",end =' ')
    else:
        print("0", end=' ')
