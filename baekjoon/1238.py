from sys import stdin
from heapq import heappop,heappush

INF = 100*10000
distance_table = [] 

def dijkstra(start_node,graph):
    min_list = [INF]*n
    priority_queue = []
    min_list[start_node] = 0
    heappush(priority_queue,(0,start_node))
    while len(priority_queue) > 0:
        min_distance,now_node = heappop(priority_queue)
        for connected_node,distance in filter(lambda x : x[1] != -1,enumerate(graph[now_node])):
            if min_distance + distance < min_list[connected_node]:
                min_list[connected_node] = min_distance + distance
                heappush(priority_queue,(min_distance+distance,connected_node))
    return min_list 


n,m,x = map(int,stdin.readline().strip().split())
graph = [[-1]*n for _ in range(n)]
reversed_graph = [[-1]*n for _ in range(n)]

for _ in range(m):
    first,second,distance = map(int,stdin.readline().strip().split())
    graph[first-1][second-1] = distance
    reversed_graph[second-1][first-1] = distance
max_time = 0
x_to_towns_distances = dijkstra(x-1,graph)
towns_to_x_distances = dijkstra(x-1,reversed_graph) 

for node in range(n):
    max_time = max(x_to_towns_distances[node] + towns_to_x_distances[node],max_time) 
print(max_time)
    
    