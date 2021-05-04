from sys import stdin
from collections import deque

visited = set()
nodeDict = dict()
connected = 0

def bfs(start):
    global connected
    q = deque()
    visited.add(start)
    q.append(start)
    while len(q) != 0:
        now = q.pop()
        for i in nodeDict[now]:
            if i not in visited:
                visited.add(i)
                q.append(i)
    connected += 1
    
n,m = map(int,stdin.readline().strip().split())

for i in range(m):
    u,v = map(int,stdin.readline().strip().split())
    if u in nodeDict:
        nodeDict[u].append(v)
    else:
        nodeDict[u] = [v]
    if v in nodeDict:
        nodeDict[v].append(u)
    else:
        nodeDict[v] = [u]

for i in range(1,n+1):
    if i not in nodeDict:
        connected += 1
    if i in nodeDict and i not in visited:
        bfs(i)
print(connected)