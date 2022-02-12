from sys import stdin
import heapq

"""
    전략 : 다익스트라 알고리즘으로 통해 이동하기
"""

def delivary():
    """
        다익스트라 알고리즘을 이용해서 택배를 배송하는 함수
    """
    dist[1] = 0
    pq = []
    heapq.heappush(pq,(0,1)) # 우선 순위큐에 (소의 수, 가는 헛간)을 넣기
    while (len(pq) > 0):
        cost,node =heapq.heappop(pq)
        for road in graph[node]:
            new_cost,new_node = road
            if node == new_node:
                continue
            if dist[node] + new_cost < dist[new_node]:
                dist[new_node] = dist[node] + new_cost
                heapq.heappush(pq, (dist[new_node],new_node))
n,m = map(int,stdin.readline().strip().split())
dist = [1001*50000]*(n+1)
graph = {}

for node in range(1,n+1):
    graph[node] = [] 

for i in range(m):
    a,b,c = map(int,stdin.readline().strip().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
delivary()
print(dist[n])