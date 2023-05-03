from sys import stdin
from collections import deque
"""
    내용이 2차원 리스트를 만들어서 그래프를 구현하기 
"""

def visit(node):
    global visit_count
    queue = deque()
    visited[node] = visit_count
    queue.append(node)
    while len(queue) > 0:
        now_node = queue.popleft()
        for next_node in graph[now_node]:
            if visited[next_node] == 0:
                visit_count += 1
                visited[next_node] = visit_count
                queue.append(next_node)

n,m,r = map(int,stdin.readline().strip().split())
visited = [0] * (n+1)
visit_count = 1
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = map(int,stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

for connected_nodes in graph:
    connected_nodes.sort(reverse=True)

visit(r)
for visit_count in visited[1:]:
    print(visit_count)