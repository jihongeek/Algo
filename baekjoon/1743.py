from sys import stdin
from collections import deque

def isValid(location):
    global h,w
    return 0 <= location[0] < h and 0 <= location[1] < w

def getLocationsToMove(location):
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    locations = [(location[0] + moves[i][0],location[1] + moves[i][1]) for i in range(4)]
    return filter(isValid,locations)

def bfs(row,col):
    visited[row][col] = True
    trash = 1
    q = deque()
    q.append((row,col))
    while len(q) > 0:
        location = q.popleft()
        for newLocation in getLocationsToMove(location):
            newRow,newCol = newLocation
            if not visited[newRow][newCol] and way[newRow][newCol]:
                visited[newRow][newCol] = True
                trash += 1
                q.append((newRow,newCol))            
    return trash


h,w,k = map(int, stdin.readline().strip().split())
way = [[False]*w for _ in range(h)]
visited = [[False]*w for _ in range(h)]
trashMax = 0
for _ in range(k):
    trashRow,trashCol = map(int,stdin.readline().strip().split())
    way[trashRow-1][trashCol-1] = True
for row in range(h):
    for col in range(w):
        if not visited[row][col] and way[row][col]:   
            trashMax = max(trashMax,bfs(row,col))
print(trashMax)
