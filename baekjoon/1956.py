from sys import stdin 

"""
    전략:
    플로이드-워셜 방식으로 최소가 되는 사이클을 찾는다.
    일방통행 -> 단방향 그래프
"""
v,e = map(int,stdin.readline().strip().split())
infinite_distance = 10001*(400)*(400-1)
map_of_city = [[infinite_distance]*v for _ in range(v)]

for _ in range(e):
    a,b,distance = map(int,stdin.readline().split())
    map_of_city[a-1][b-1] = distance

min_cycle = infinite_distance

for k in range(v):
    for i in range(v):
        for j in range(v):
            if map_of_city[i][k] + map_of_city[k][j] < map_of_city[i][j]:
                map_of_city[i][j] = map_of_city[i][k] + map_of_city[k][j]

for town in range(v):
    min_cycle = min(min_cycle, map_of_city[town][town])

if min_cycle == infinite_distance:
    print(-1)
else:
    print(min_cycle)