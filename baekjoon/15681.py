from sys import stdin, setrecursionlimit
"""

    트리의 각 노드를 포함하는 서브트리의 정점의 수를
    재귀를 통해 구해서 리스트에 넣어두고,
    쿼리가 들어오면 출력하기 
    "주의사항 : 이 코드에서 리스트의 0번째 인덱스 공간을 사용하기 위해 
    노드번호 - 1을 해서 풀었다. 
"""

# 재귀를 사용해서 풀기 때문에 파이썬의 재귀 제한 (종특)을 풀어줘야 한다.
setrecursionlimit(100000)

n,r,q = map(int, stdin.readline().strip().split())

# 트리와 노드의 수를 저장할 리스트 만들기
tree = [ [] for _ in range(n) ]
node_counts = [0]*n

# (서브)트리의 정점 갯수를 세는 함수 : 재귀함수로 구현
def count_nodes(node, parent):
    result = 1 
    for child in tree[node]:
        if child == parent:
            continue
        result += count_nodes(child,node)
    node_counts[node] += result
    return node_counts[node]
     

# 노드 입력 받아 트리 리스트에 표시
for _ in range(n-1):
    node1,node2 = map(int,stdin.readline().strip().split())
    tree[node1-1].append(node2-1)
    tree[node2-1].append(node1-1)

# 트리의 노드 갯수 세기 
count_nodes(r-1,n+1)

# 쿼리 입력 받아, 센 노드의 갯수 출력
for _ in range(q):
    node = int(stdin.readline().strip())
    print(node_counts[node-1])
