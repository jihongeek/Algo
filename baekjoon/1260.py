from sys import stdin 
from collections import deque
def search(v,stype):
    global n
    visited = [False]*n
    deq = deque()
    visited[v-1] = True
    deq.append(v-1)
    while len(deq) > 0:
        now = deq.popleft() if stype == "bfs" else deq.pop() 
        print(now+1,end =" ")
        for i in range(n):
            if graph[now][i] and not visited[i]:
                visited[i] = True
                deq.append(i)
    print()
            
n,m,v = map(int, stdin.readline().strip().split()) 
graph = [[False]*n for _ in range(n)]
for i in range(m):
    row,col = map(int, stdin.readline().strip().split())
    graph[row-1][col-1] = True
search(v,"dfs")
search(v,"bfs")

    

