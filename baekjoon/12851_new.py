from sys import stdin
from collections import deque
"""
    전략 : 현재 최단시간 및 위치 별 최단시간 저장해놓고
    위치별 최단시간 보다 작거나 같아야 이동하게 하기 
    """

# i까지의 경로의 최단 시간 visited[i][0], 그 방법의 수 visited[i][1]
visited = [(100000,0) for _ in range(100001)]
n,k = map(int,stdin.readline().strip().split())
def is_visitable(location,now_time):
    global visited
    if not 0 <= location <= 100000:
        return False
    if not now_time <= visited[location][0]:
        return False
    # k로 가는 경로를 이미 찾았는 데, 더 먼 경로로 이동하면 안된다.
    if visited[k][1] > 0 and now_time > visited[k][0]:
        return False 
    return True

def visit(start):
    global k
    visited[start] = (0,1)
    q = deque()
    q.append((start,0))
    while len(q) > 0:
        location,time = q.popleft()
        next_locations = (location+1,location-1,2*location)
        for next_location in next_locations:
            if is_visitable(next_location,time+1) is True:
                # 다음 위치까지의 시간을 최신으로 갱신 해주기
                if time + 1 < visited[next_location][0]:
                    visited[next_location] = (time+1,1)
                elif time + 1 == visited[next_location][0]:
                    visited[next_location] = (time+1,visited[next_location][1] + 1)
                q.append((next_location,time+1))
visit(n)
print(visited[k][0])
print(visited[k][1])

