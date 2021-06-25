from sys import stdin 
from collections import deque
rowMove = [0,0,1,-1]
colMove = [1,-1,0,0]

def bfs(land : tuple):
    minDist = 25000
    global maxDist, visited, rowMove, colMove
    q = deque()
    visited[land[0]][land[1]] = True
    q.append(land)
    while len(q) > 0:
        isblocked = True
        now = q.pop()
        for i in range(3):
            row = now[0] + rowMove[i]
            col = now[1] + colMove[i]
            if row >= 0 and col >= 0 and row < h and col < w :
                if island[row][col] == "L" and not visited[row][col]:
                    visited[row][col] = True
                    q.append((row,col,now[2]+1))
                    isblocked = False
        if isblocked:
            minDist = min(minDist,now[2])
    return minDist

maxTime = 0
h,w = map(int, stdin.readline().strip().split())
island = [stdin.readline().strip() for _ in range(h)] 

for row in range(h):
    for col in range(w):
        if island[row][col] == "L":
            visited = [[False]*w for _ in range(h)]
            maxTime = max(bfs((row,col,0)),maxTime)      
print(maxTime)  