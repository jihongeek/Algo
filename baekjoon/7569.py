from collections import deque
import sys

def bfs():
    dx = [-1,1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]
    day = -1
    while len(q) != 0:
        z, y, x = q.popleft()
        for i in range(6):
            now_x = x + dx[i]
            now_y = y + dy[i]
            now_z = z + dz[i]
            if now_x < m and now_x >= 0 and now_y < n and now_y >= 0 and now_z < h and now_z >= 0:
                if box[now_z][now_y][now_x] == -1:
                    continue
                if (not visited[now_z][now_y][now_x]) and box[now_z][now_y][now_x] == 0:
                    visited[now_z][now_y][now_x] = True
                    box[now_z][now_y][now_x] = box[z][y][x] + 1
                    q.append((now_z, now_y, now_x))
    day =  box[z][y][x] - 1
    
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    day = -1
                    break
    return day

q = deque()

m, n, h = tuple(map(int,input().split()))

visited = [ [ [False]*m for x in range(n) ] for floor in range(h) ]

box = [ [ list(map(int,sys.stdin.readline().split())) for x in range(n) ] for floor in range(h) ]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if (not visited[i][j][k]) and box[i][j][k] == 1:
                visited[i][j][k] = True
                q.append((i,j,k))           
ans = bfs()
print(ans)
