'''
[트리] 트리순회 (실1)
dfs?
전위: 루트->왼->오
중위 : 왼 ->루트->오
후위: 왼->오->루트

- 항상 A가 루트 노드
- '.' : 자식 노드 (X) 뜻
goal: 전위 순회,중위 순회, 후위 순회한 결과를 출력
'''
import sys
input = sys.stdin.readline


n = int(input())
#딕셔너리 -> '트리' 만들자
#{'A': ('B', 'C'), 'B': ('D', '.'), 'C': ('E', 'F'),
#'E': ('.', '.'), 'F': ('.', 'G'), 'D': ('.', '.'), 'G': ('.', '.')}
tree = {}
for i in range(n):
    node,left,right = input().split()
    tree[node] = left, right

# print(tree)

#전위 순회 (루트>왼>오)
def preorder(x):
    if x != '.': #루트 노드한테 자식이 존재('.':자식이 없다)
        print(x, end='')
        #루트노드 기준 -> 왼쪽노드 탐색
        preorder(tree[x][0])
        # 루트노드 기준 -> 오른쪽노드 탐색
        preorder(tree[x][1])

#중위 순회 (왼>루트>오)
def midorder(x):
    if x != '.': #루트 노드한테 자식이 존재('.':자식이 없다)
        #루트노드 기준 -> 왼쪽노드부터 탐색
        midorder(tree[x][0])
        print(x, end='')
        # 루트노드 기준 -> 오른쪽노드 탐색
        midorder(tree[x][1])

#중위 순회 (왼>오>루트)
def postorder(x):
    if x != '.': #루트 노드한테 자식이 존재('.':자식이 없다)
        #루트노드 기준 -> 왼쪽노드부터 탐색
        postorder(tree[x][0])
        # 루트노드 기준 -> 오른쪽노드 탐색
        postorder(tree[x][1])
        print(x, end='')

preorder('A')
print()
midorder('A')
print()
postorder('A')
