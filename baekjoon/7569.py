from queue import Queue

def bfs():
    dx = [-1,1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]
    z,y,x = q.get()

    for i in range(6):
        now_x = x + dx[i]
        now_y = y + dy[i]
        now_z = z + dz[i]
        if now_x < m and now_x >= 0 and now_y < n and now_y >= 0 and now_z < h and now_z >= 0:
            if not visited[now_z][now_y][now_x]:
                visited[now_z][now_y][now_x] = True
                box[now_z][now_y][now_x] = box[now_z][now_y][now_x] + box[z][y][x]    
                q.put((now_z,now_y,now_x))
    day =  box[z][y][x] - 1
    
    for i in range(h):

q = Queue()

m, n, h = tuple(map(int,input().split()))

visited = [ [ [False]*m for x in range(n) ] for floor in range(h) ]

box = [ [ list(map(int,input().split())) for x in range(n) ] for floor in range(h) ]


print(box)
print(visited)