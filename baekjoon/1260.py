from sys import stdin 
from collections import deque
def bfs(v):
    global n
    visited = [False]*n
    q = deque()
    visited[v-1] = True
    print(v,end = " ")
    q.append(v-1)
    while len(deq) > 0:
        now = deq.popleft()
        for i in range(n):
            if graph[now][i] and not visited[i]:
                visited[i] = True
                print(i+1,end = " ")
                q.append(i)
def dfs(v,visited : list):
    global n
    visited[v-1] = True
    print(v, end= " ")
    isEnd = False
    for i in range(n):
        if graph[v-1][i] and not visited[i]:
            visited[i] = True
            dfs(i+1,visited) 
            continue 
        else:
            isEnd = True
    if isEnd:
        return

    
    
            
n,m,v = map(int, stdin.readline().strip().split()) 
graph = [[False]*n for _ in range(n)]
for i in range(m):
    row,col = map(int, stdin.readline().strip().split())
    graph[row-1][col-1] = True
    graph[col-1][row-1] = True
dfs(v, [False]*n)
print()
bfs(v)

    

