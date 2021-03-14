# Python의 큐 라이브러리
from collections import deque

# row : 행의 인덱스를 나타냄 col : 열의 인덱스를 나타냄
def bfs(row,col):
    # 구역 내부에 있는 양의 수와 늑대의 수를 저장하는 변수
    wolf = 0
    sheep = 0

    # 상하좌우를 탐색할 때 사용하는 리스트
    rowMove = [0,0,1,-1]
    colMove = [1,-1,0,0]

    # bfs에 사용되는 큐 
    q = deque()
    
    # 방문 표시 
    visited[row][col] = True
    q.append((row,col))
    while (len(q) > 0):
        row,col = q.popleft()
        if backyard[row][col] == 'o':
            sheep += 1
        elif backyard[row][col]== 'v':
            wolf += 1
        for i in range(4):
            nowCol = col + colMove[i]
            nowRow = row + rowMove[i]
            if nowCol >= 0 and nowCol < C and nowRow >= 0 and nowRow < R:
                if backyard[nowRow][nowCol] != '#' and visited[nowRow][nowCol] == False:
                    visited[nowRow][nowCol] = True
                    q.append((nowRow,nowCol))
            else:
                return (0,0)
    if sheep > wolf:
        wolf = 0
    else:
        sheep = 0
    return (wolf , sheep)
            
allWolf,allSheep = (0,0) 
R,C = map(int,input().split())
backyard = [ list(input()) for _ in range(R) ]
visited = [ [False]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if visited[i][j] == False and backyard[i][j] != '#':
            wolf,sheep = bfs(i,j)
            allWolf += wolf
            allSheep += sheep

print(f"{allSheep} {allWolf}")