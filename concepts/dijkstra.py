from sys import stdin
from heapq import heappop,heappush
import time

def djikstra_naive(start_node):
    confirmed_nodes = [False] * n
    min_list = [INF] * n
    confirmed_count = 0    
    
    # 시작 노드일 경우 확정 시키기
    confirmed_nodes[start_node] = True
    min_list[start_node] = 0
    confirmed_count += 1    
    # 확정한 노드와 연결된 노드도 거리 최신화 해주기
    for end_node,weight in filter(lambda x : x[1] != -1,enumerate(graph[start_node])):
        min_list[end_node] = min(weight,min_list[end_node])

    while confirmed_count < n:
        # 확정된 노드를 제외하고 가장 작은 노드를 찾아서 확정한다. 
        min_distance = INF
        min_node = 0
        for node in range(n):
            if confirmed_nodes[node] is False and min_list[node] < min_distance:
                min_distance = min_list[node]
                min_node = node
        confirmed_nodes[min_node] = True
        confirmed_count += 1 
        # 확정된 노드와 연결된 노드 사이의 최단거리를 최신화 한다.
        for end_node,weight in filter(lambda x : x[1] != -1,enumerate(graph[min_node])):
            if confirmed_nodes[end_node] is False: 
                min_list[end_node] = min(min_list[min_node]+weight,min_list[end_node])
    print(min_list)

def djikstra_fast(start_node):
    min_list = [INF] * n
    
    # 시작 노드일 경우 확정 시키기
    min_list[start_node] = 0
    priority_queue = []
    #(시작 부터 노드까지의 거리, 노드)
    heappush(priority_queue,(0,start_node))
    
    while len(priority_queue) > 0:
        min_distance,now_node = heappop(priority_queue)
        for connected_node,weight in filter(lambda x : x[1] != -1,enumerate(graph[now_node])):
            if min_distance + weight < min_list[connected_node]:
                min_list[connected_node] =  min_distance + weight
                heappush(priority_queue,(min_distance+weight,connected_node))
    print(min_list)

n,m = map(int,stdin.readline().strip().split())
number_of_nodes = n
# 무한 값 설정
INF = 100000
shortest_distance = [INF] * number_of_nodes
graph = [[-1] * number_of_nodes for _ in range(number_of_nodes)]

for _ in range(m):
    start,end,weight = map(int,stdin.readline().strip().split()) 
    graph[start-1][end-1] = weight

# 시간 비교
start_naive = time.time()
djikstra_naive(0)
end_naive = time.time()

start_fast = time.time()
djikstra_fast(0)
end_fast = time.time()

print(end_naive-start_naive,"vs",end_fast-start_fast)