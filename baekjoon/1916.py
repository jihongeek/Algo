from sys import stdin
from heapq import heappop,heappush
INF = 1000*100000*100000

def dijkstra(start_node):
    priority_queue = []
    min_list = [INF]*n
    
    min_list[start_node] = 0
    heappush(priority_queue, (0,start_node))
    
    while len(priority_queue) > 0:
        min_cost,node = heappop(priority_queue)
        if min_cost > min_list[node]:
            continue
        for connected_node,cost in graph[node]:
            if min_cost + cost < min_list[connected_node]:
                min_list[connected_node] = min_cost + cost
                heappush(priority_queue,(min_cost+cost,connected_node))
    return min_list

n = int(stdin.readline().strip())
m = int(stdin.readline().strip())
graph = [[] for _ in range(n)]

for _ in range(m):
    departure,arrival,cost = map(int,stdin.readline().strip().split())
    graph[departure-1].append((arrival-1,cost))

departure_to_find,arrival_to_find = map(int,stdin.readline().strip().split())
print(dijkstra(departure_to_find-1)[arrival_to_find-1])