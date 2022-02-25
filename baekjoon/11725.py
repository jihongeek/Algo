from sys import stdin,setrecursionlimit 

#python의 재귀제한을 10^9 까지 올려주자 아니면 에러가 발생한다!
setrecursionlimit(10**9)
"""
    인접행렬은 필요없다. -> 트리는 사이클이 없다. 
    -> 연결이 최대의 경우에 2*100000 이기 때문이다?
    트리를 딕셔너리와 리스트로 구현하고 dfs를 하자
"""

def find_parent(node):
    for child in tree[node]:
        if not visited[child]:
            visited[child] = True 
            parents[child] = node
            find_parent(child)
n = int(stdin.readline().strip())
tree = {}
visited = [False]*(n+1)
parents = [-1]*(n+1)
for _ in range(n-1):
    node1,node2 = map(int,stdin.readline().strip().split())
    if node1 not in tree:
        tree[node1] = []
    if node2 not in tree:
        tree[node2] = []
    tree[node1].append(node2)
    tree[node2].append(node1)

find_parent(1)
for parent in parents[2:]:
    print(parent)