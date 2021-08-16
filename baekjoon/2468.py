from sys import stdin
from collections import deque

def isValid(location):
    return 0 <= location[0] < n and 0 <= location[1] < n
    
def getLocationsToMove(location):
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    locations = [ (location[0]+move[0], location[1]+move[1]) for move in moves]
    return list(filter(isValid,locations))

def bfs(rowNum,colNum):
    visited[rowNum][colNum] = True
    q = deque()
    q.append((rowNum,colNum))
    while len(q) > 0:
        location = q.popleft()
        for newLocation in getLocationsToMove(location):
            newRowNum,newColNum = newLocation
            if not visited[newRowNum][newColNum] and region[newRowNum][newColNum] > height:
                visited[newRowNum][newColNum] = True
                q.append((newRowNum,newColNum))
    return 1

n = int(stdin.readline().strip())
maxHeight = 0
maxSafeArea = 0
region = []

for rowNum in range(n):
    row = stdin.readline().strip().split()
    for colNum in range(n):
        height = int(row[colNum])
        maxHeight = max(height,maxHeight)
        row[colNum] = height
    region.append(row)

for height in range(maxHeight-1,-1,-1):
    safeArea = 0
    visited = [[False]*n for _ in range(n)]
    for rowNum in range(n):
        for colNum in range(n):
            if not visited[rowNum][colNum] and region[rowNum][colNum] > height:
                safeArea += bfs(rowNum,colNum)
    maxSafeArea = max(safeArea,maxSafeArea)                
print(maxSafeArea)
        
        