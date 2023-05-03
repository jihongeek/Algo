from sys import stdin
from collections import deque

def is_visitable(location):
    if not 0 <= location <= 100000:
        return False
    if visited[location] == True:
        return False
    return True

def find(location):
    minimum_time = 100000
    time = 0
    visited[location] = True
    queue = deque()
    queue.append((location,time))
    while len(queue) > 0:
        now_location,now_time = queue.popleft()
        if now_location == k:
            minimum_time = min(minimum_time,now_time) 
        if is_visitable(now_location - 1):
            visited[now_location - 1] = True
            queue.append((now_location - 1,now_time+1))
        
        if is_visitable(now_location + 1):
            visited[now_location + 1] = True
            queue.append((now_location + 1,now_time+1)) 
        
        if is_visitable(2*now_location):
            visited[2*now_location] = True
            queue.append((2*now_location,now_time+1)) 
    return minimum_time    

n,k = map(int,stdin.readline().strip().split())
visited = [False] * 100001
print(find(n))
