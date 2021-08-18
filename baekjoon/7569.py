from sys import stdin 
from collections import deque

def bfs():
    global unripeTomato,maxDay,q
    unripeToRipe = -len(q)
    day = 0
    while len(q) > 0:
        location = q.popleft()
        layerNum,rowNum,colNum,dayOfRipeness = location
        box[layerNum][rowNum][colNum] = 1
        unripeToRipe += 1
        day = max(day,dayOfRipeness)
        if layerNum - 1 >= 0 and not visited[layerNum-1][rowNum][colNum] and box[layerNum-1][rowNum][colNum] == 0:
            visited[layerNum-1][rowNum][colNum] = True
            q.append((layerNum-1,rowNum,colNum,dayOfRipeness+1))
        if layerNum + 1 < h and not visited[layerNum+1][rowNum][colNum] and box[layerNum+1][rowNum][colNum] == 0:
            visited[layerNum+1][rowNum][colNum] = True
            q.append((layerNum+1,rowNum,colNum,dayOfRipeness+1))
        if rowNum - 1 >= 0 and not visited[layerNum][rowNum-1][colNum] and box[layerNum][rowNum-1][colNum] == 0:
            visited[layerNum][rowNum-1][colNum] = True
            q.append((layerNum,rowNum-1,colNum,dayOfRipeness+1))
        if rowNum + 1 < n and not visited[layerNum][rowNum+1][colNum] and box[layerNum][rowNum+1][colNum] == 0:
            visited[layerNum][rowNum+1][colNum] = True
            q.append((layerNum,rowNum+1,colNum,dayOfRipeness+1))
        if colNum - 1 >= 0 and not visited[layerNum][rowNum][colNum-1] and box[layerNum][rowNum][colNum-1] == 0:
            visited[layerNum][rowNum][colNum-1] = True
            q.append((layerNum,rowNum,colNum-1,dayOfRipeness+1))
        if colNum + 1 < m and not visited[layerNum][rowNum][colNum+1] and box[layerNum][rowNum][colNum+1] == 0:
            visited[layerNum][rowNum][colNum+1] = True
            q.append((layerNum,rowNum,colNum+1,dayOfRipeness+1))
    
    maxDay = max(maxDay,day)
    unripeTomato -= unripeToRipe

m,n,h = map(int,stdin.readline().strip().split())
unripeTomato = 0
maxDay = 0
box = []
for layerNum in range(h):
    board = []
    for rowNum in range(n):
        row = stdin.readline().strip().split()
        for colNum in range(m):
            row[colNum] = int(row[colNum])
            if row[colNum] == 0:
                unripeTomato += 1 
        board.append(row)
    box.append(board)

visited = [[[False]*m for j in range(n)] for i in range(h)]
q = deque()

for layer in range(h):
    for row in range(n):
        for col in range(m):
            if not visited[layer][row][col] and box[layer][row][col] == 1:
                visited[layer][row][col] = True
                q.append((layer,row,col,0))
bfs()
if unripeTomato != 0:
    print(-1)
else:
    print(maxDay)