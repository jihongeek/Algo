from sys import stdin
import heapq
"""
    전략 :
    그래프를 딕셔너리에 출발노드 : [(가중치,도착 노드)...] 로 나타낸다.
    거리를 저장할 리스트를 만든다. "기본값은 (최대 길이 + 1) * 최대간선 갯수"
    다익스트라를 계산할 때 heapq을 사용한다. (거리,노드)
    + 방문 표시를 하지 않고 다익스트라를 진행해도 가능하나, -> 왜 이렇게 되는 지 모르겠음
      방문 표시를 하면 속도가 빨라지지 않을까? -> 다시 방문해야 더 빠를 수도 있다.
"""

graph = {}
def dijkstra(start_node):
    pq = []
    dist[start_node] = 0
    heapq.heappush(pq,(0,start_node))
    while len(pq) > 0:
        cost,node = heapq.heappop(pq)
        if dist[node] < cost:
            continue
        for edge in graph[node]:
            new_cost,new_node = edge
            if dist[new_node] > dist[node]+new_cost:
                dist[new_node] = dist[node]+new_cost
                heapq.heappush(pq,(dist[new_node],new_node))


v,e = map(int,stdin.readline().strip().split())
dist = [(10 + 1)*300000]*(v+1)
visited = [False]*(v+1)
k = int(stdin.readline().strip())

for node in range(1,v+1):
    graph[node] = []
for _ in range(e):
    start,end,cost = map(int, stdin.readline().strip().split())
    graph[start].append((cost,end))

dijkstra(k)

for node in range(1,v+1):
    if dist[node] == (10 + 1)*300000:
        print("INF")
    else:
        print(dist[node])