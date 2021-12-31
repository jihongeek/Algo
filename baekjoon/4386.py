from sys import stdin 
from math import sqrt
def find(node_index):
    while graph[node_index] > -1:
        node_index = graph[node_index]
    return node_index

def union(node1_index, node2_index):
    node1_parent, node2_parent = find(node1_index),find(node2_index)
    if node1_parent == node2_parent:
        return
    if graph[node1_parent] <= graph[node2_parent]:
        graph[node1_parent] += graph[node2_parent]
        graph[node2_parent] = node1_parent
    else:
        graph[node2_parent] += graph[node1_parent]
        graph[node1_parent] = node2_parent
    

def get_distance(location1, location2):
    return sqrt(pow(location1[0] - location2[0],2) + pow(location1[1] - location2[1],2)) 
n = int(stdin.readline().strip())
graph = [-1]*n
sum_of_cost = 0
node_locations = []
edges = []

for _ in range(n):
    x,y = map(float, stdin.readline().strip().split())
    node_locations.append((x,y))

# (노드인덱스1, 노드인덱스2, 거리(가중치))를 원소로 하는 리스트 만들고 정렬
for node1 in range(len(node_locations)):
    for node2 in range(node1+1,len(node_locations)):
        distance = get_distance(node_locations[node1], node_locations[node2])
        edges.append((node1,node2,distance))
edges = sorted(edges, key= lambda x : x[2])

for edge in edges:
    node1_parent, node2_parent = find(edge[0]),find(edge[1])
    if node1_parent != node2_parent:
        sum_of_cost += edge[2]
        union(edge[0],edge[1])
print("%.2f"%sum_of_cost)