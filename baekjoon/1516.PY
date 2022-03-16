from sys import stdin 
from collections import deque

n = int(stdin.readline().strip())
build_times = [0]
build_graph = [ [] for _ in range(n+1)]
in_degree = [0]*(n+1)
q = deque()

for build_num in range(1,n+1):
    build_info = list(map(int,stdin.readline().strip().split()))
    # 건설 시간 저장
    build_time = build_info[0]
    build_times.append(build_time)
    # 먼저 지어야하는 건물 그래프에 표시
    for build_before in build_info[1:]:
        if build_before == -1:
            break  
        build_graph[build_before].append(build_num)
        # 진입 차수 저장
        in_degree[build_num] += 1

results = [] + build_times
for build_num in range(1,n+1):
    if in_degree[build_num] == 0:
        q.append(build_num)

while len(q) > 0:
    now_build_num = q.popleft()
    for next_build_num in build_graph[now_build_num]:
        results[next_build_num] = max(results[next_build_num],results[now_build_num]+build_times[next_build_num])
        in_degree[next_build_num] -= 1
        if in_degree[next_build_num] == 0:
            q.append(next_build_num) 
    build_graph[now_build_num] = []
for min_time in results[1:]:
    print(min_time)