from sys import stdin

"""
    dfs를 통해 각 노드에서 리프노드까지의 거리들을 구하고, 
    각 노드마다 가장 긴 두거리의 합을 지름으로 하여 최댓값을 구한다.
"""

def dfs(parent,weight):
    max_distance = 0
    if len(tree[parent]) == 0:
        return weight
    for child,child_weight in tree[parent]:
        distance = dfs(child,child_weight)
        node_distances[parent].append(distance)
        max_distance = max(distance,max_distance)
    return max_distance + weight
        
n = int(input())
node_distances = [[] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent,child,weight = map(int,stdin.readline().strip().split())
    tree[parent].append((child,weight))
tree[0].append((1,0))
dfs(0,0)
diameter = 0
for distance_list in node_distances:
    if len(distance_list) == 1:
        diameter = max(diameter,distance_list[0])
    elif len(distance_list) > 1:
        distance_list.sort(reverse=True)
        diameter = max(diameter,distance_list[0]+distance_list[1])
print(diameter)

        