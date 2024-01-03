from sys import stdin
from collections import deque
"""
    bfs를 하는데 그람을 찾았을 때에는 큐에 넣을 때 
    표시해줘서 벽에 상관없이 갈 수 있게하기
    그람이 없을 수도? -> 큐가 비었는데도 공주님을 못찾았거나
    공주님을 구하는 시간이 T보다 크면 실패

    그람을 발견했을 때는 방문표시 따로 하기
    -> 그람을 먹는게 그냥 가는거 보다 손해인 경우가 있기에 
    bfs를 아예 처음부터 하는 건 X
"""

def is_visitable(row,col,is_sword_founded):
    if not (1 <= row <= n):
        return False
    if not (1 <= col <= m):
        return False
    if (visited[row][col] is True and 
        is_sword_founded is False):
        return False
    if (castle[row][col] == "1" and
        is_sword_founded is False):
        return False
    if (visited_for_sword[row][col] is True and 
        is_sword_founded is True):
        return False
    
    return True  

def rescue(start_row,start_col,t):
    global visited
    is_princess_rescued = False
    min_time = n * m + 1
    queue = deque()
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    visited[start_row][start_col] = True
    queue.append((start_row,start_col,0,False))
    
    while len(queue) > 0:
        row,col,time,is_sword_founded = queue.popleft()
        if castle[row][col] == "2" and is_sword_founded is False:
            is_sword_founded = True
        if row == n and col == m:
            visited[row][col] = False
            is_princess_rescued = True
            min_time = min(time,min_time)

        for move in moves:
            row_move,col_move = move
            next_row = row + row_move
            next_col = col + col_move
            if is_visitable(next_row,next_col,is_sword_founded):
                if is_sword_founded is True:
                    visited_for_sword[next_row][next_col] = True
                else:
                    visited[next_row][next_col] = True
                queue.append((next_row,next_col,time+1,is_sword_founded))
    if (is_princess_rescued == False or
        min_time > t):
        return "Fail"
    else:
        return min_time
        
n,m,t = map(int,stdin.readline().strip().split())
visited = [[False]*(m+1) for _ in range(n+1)]
visited_for_sword = [[False]*(m+1) for _ in range(n+1)]
castle = []
castle.append([" "]*(m+1))
for _ in range(n):
    castle.append([""] + stdin.readline().strip().split())
print(rescue(1,1,t))
