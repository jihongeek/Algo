from sys import stdin
from collections import deque

"""
주사위 굴리기 -> 현재 칸에서 다음 칸으로 주사위 눈 수만 큼 이동
주사위를 6가지 방법으로 던져서 한번에 1..6칸으로 가게 해서 만약에
해당 칸에 다른 칸으로 이동해야하는 경우(뱀+사다리)면 이동해버리기
큐에 현재말의 위치와 주사위를 던진 횟수를 저장하면 될 거 같다.

bfs를 위해서는 큐와, 방문을 표시하는 게 있어야 한다. 

"""
roll_count = 0
board = [location for location in range(101)]
visited = [False]*101

def bfs(start_num):
    visited[start_num] = True
    q = deque()
    q.append((start_num,0))
    while len(q) > 0:
        now_location,now_roll_count = q.popleft()
        if now_location == 100:
            return now_roll_count
        for dice_eye in range(1,6+1):
            if now_location + dice_eye <= 100 and not visited[now_location + dice_eye]:
                visited[now_location+dice_eye] = True
                visited[board[now_location+dice_eye]] = True
                q.append((board[now_location+dice_eye],now_roll_count+1))

n,m = map(int,stdin.readline().strip().split())

for i in range(n):
    start,end = map(int,stdin.readline().strip().split())
    board[start] = end
for i in range(m):
    start,end = map(int,stdin.readline().strip().split())
    board[start] = end
print(bfs(1))





