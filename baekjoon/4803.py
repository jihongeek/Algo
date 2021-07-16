from sys import stdin

def union(a,b):
    global graph
    if graph[a] == graph[b] == -1:
        graph[b] = a
        return
    elif graph[a] != -1 and graph[b] == -1:
        graph[b] = a
def parent(node):
    global graph
    if graph[node] == -1:
        return node
    return parent(graph[node])
case = 1
while True:
    n,m = map(int,stdin.readline().strip().split())
    if n + m == 0:
        break
    graph = [-1]*n
    tree = 0
    for _ in range(m):
        a,b = map(int,stdin.readline().strip().split())
        union(a-1,b-1)
    for node in graph:
        if node == -1:
            tree += 1
    if tree == 0:
        print(f"Case {case}: No trees.")
    elif tree == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {tree} trees.")
    case+=1


