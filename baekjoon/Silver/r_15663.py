'''
[백트래킹] N과 M(9) (실2)
1. 중복 x
1 7 9 9 라고 해서 19, 19(X)
=> 이미 한 번 조회한 애를 또 꺼내면 안됨
2. 사전순으로

'''

n,m = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()

result = []
prev = 0 #직전 값
visited = [False] * n   # [1,0,0,0] => [1,7,9,9]


def f(depth):
    prev = 0

    if depth == m:
        # print(visited)
        print(' '.join(map(str,result)))
        return

    for i in range(n):
        #이전과 동일한 값이 또 나왔나? && 방문한적이 있나?
        #ㄴ>우리가 앞에서 sort()를 해줬으므로 중복된 값이 바로 나오는지 따짐

        # print("arr[i] = %d 현재 prev = %d" %(arr[i], prev)) 11
        if arr[i] != prev and visited[i] == False:
            result.append(arr[i]) #1 11
            prev = arr[i]  #1
            print("prev %d,"%prev)
            # print(result)

            visited[i] = True #방문
            f(depth + 1) #함수호출  # 17  19   prev => 7 9
            result.pop()
            visited[i] = False

f(0)
