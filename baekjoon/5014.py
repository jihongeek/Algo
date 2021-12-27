from sys import stdin
from collections import deque

visited_floor_set = set()

def go_to_target_floor(start_floor, up_button, down_button, target_floor):
    visited_floor_set.add(start_floor)
    visit_queue = deque()
    visit_queue.append((start_floor,0))
    while len(visit_queue) > 0:
        visited_floor,press_count = visit_queue.popleft()

        # 층에 도착시 버튼을 눌렀던 횟수 출력
        if visited_floor == target_floor:
            return press_count 

        # 범위, 방문 여부 확인 후, 큐에 넣기
        if visited_floor + up_button <= f and visited_floor + up_button not in visited_floor_set:
            visited_floor_set.add(visited_floor + up_button)
            visit_queue.append((visited_floor + up_button,press_count+1))
        if visited_floor - down_button >= 1 and visited_floor - down_button not in visited_floor_set:
            visited_floor_set.add(visited_floor - down_button)
            visit_queue.append((visited_floor - down_button,press_count+1))  
    return "use the stairs"

f,s,g,u,d = map(int,stdin.readline().strip().split())

print(go_to_target_floor(s,u,d,g))
