from sys import stdin


"""
    플로이드-워셜 알고리즘을 이용해 
    모든 도시를 이동할 때의 최소값을 구한다.
"""

num_of_cities = int(stdin.readline().strip())
num_of_buses = int(stdin.readline().strip())
infinite_cost = (num_of_cities-1) * 100000 + 1
map_of_cities = [[infinite_cost]* num_of_cities for _ in range(num_of_cities)]

for _ in range(num_of_buses):
    departure,arrival,cost = map(int,stdin.readline().strip().split())
    if map_of_cities[departure-1][arrival-1] > cost:
        map_of_cities[departure-1][arrival-1] = cost 
    
for k in range(num_of_cities):
    for i in range(num_of_cities):
        for j in range(num_of_cities):
            if i == j:
                continue
            if map_of_cities[i][k] + map_of_cities[k][j] < map_of_cities[i][j]:
                map_of_cities[i][j] = map_of_cities[i][k] + map_of_cities[k][j]

for departure in range(num_of_cities):
    for arrival in range(num_of_cities):
        if map_of_cities[departure][arrival] == infinite_cost:
            print(0,end=" ")
        else:
            print(map_of_cities[departure][arrival],end=" ")
    print()
    
    