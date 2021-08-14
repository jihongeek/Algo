from sys import stdin 
from collections import deque

def isValid(location):
    global w,h
    return 0 <= location[0] < h and 0 <= location[1] < w

def getLocationsToMove(location):
    move = [ (-1,0), (1,0), (0,-1), (0,1), (1,1), (-1,-1), (1,-1), (-1,1)]
    locations = [ (location[0] + move[i][0], location[1] + move[i][1]) for i in range(8) ]
    return list(filter(isValid,locations))

def bfs(row,col):
    visited[row][col] = True
    q = deque()
    q.append((row,col))
    
    while len(q) > 0:
        location = q.popleft()
        for newLocation in getLocationsToMove(location):
            newRow,newCol = newLocation
            if visited[newRow][newCol] == False and squareMap[newRow][newCol] == "1":
                visited[newRow][newCol] = True
                q.append(newLocation)
    return 1
                
while True:
    island = 0
    w,h = map(int,stdin.readline().strip().split())
    if w == 0 and h == 0:
        break
    visited = [[False]*w for _ in range(h)]
    squareMap = [ stdin.readline().strip().replace(" ","") for _ in range(h)]
    for row in range(h):
        for col in range(w):
            if visited[row][col] == False and squareMap[row][col] == "1": 
                island += bfs(row,col)
    print(island)

    