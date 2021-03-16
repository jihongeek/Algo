from sys import stdin
from collections import deque

def bfs(person):
    global visited,n,mates
    q = deque()
    visited[person-1] = True
    q.append((person,0))
    invitedMates = 0
    while (len(q) > 0):
        nowPerson = q.pop()
        if nowPerson[1] >= 2:
            continue
        for i in range(1,n+1):
            if not visited[i-1] and mates[nowPerson[0]-1][i-1] > 0:
                visited[i-1] = True
                q.append((i,nowPerson[1]+1))
                invitedMates += 1
    return invitedMates

n = int(stdin.readline().strip())
m = int(stdin.readline().strip())
mates = [[False]*n for _ in range(n)]
visited = [False]*n 

for i in range(m):
    person1, person2 = map(int, stdin.readline().split())
    mates[person1-1][person2-1] = True
    mates[person2-1][person1-1] = True
print(bfs(1))