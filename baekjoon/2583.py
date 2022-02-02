from sys import stdin
from collections import deque
"""
    입력 받은 좌표를 이용해서 직사각형 표시하기
    왼쪽 위 -> 총 세로길이 - y1 - 직사각형 세로길이(y2-y1),x1

    세로길이 -> y2 - y1   
    가로길이 -> x2 - x1

    전략 bfs로 영역 체크하기
"""

def is_valid(new_row,new_col):
    if not (0 <= new_row < m and 0 <= new_col < n):
        return False
    if visited[new_row][new_col]:
        return False
    if not paper[new_row][new_col]:
        return False 
    return True

def check_area(row,col):
    area_size = 0
    visited[row][col] = True
    q = deque()
    q.append((row,col))
    while len(q) > 0:
        row,col = q.popleft()
        area_size += 1
        if is_valid(row-1,col):
            visited[row-1][col] = True
            q.append((row-1,col))
        if is_valid(row+1,col):
            visited[row+1][col] = True
            q.append((row+1,col))
        if is_valid(row,col-1):
            visited[row][col-1] = True 
            q.append((row,col-1))
        if is_valid(row,col+1):
            visited[row][col+1] = True
            q.append((row,col+1))    
    return area_size
        

sizes = []
m,n,k = map(int,stdin.readline().strip().split())
paper = [[True]*n for _ in range(m)]
visited = [[False]*n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int,stdin.readline().strip().split())
    height = y2 - y1
    width = x2 - x1 
    start = m - y1 - height 
    for row in range(start,start + height):
        for col in range(x1,x1 + width):
            paper[row][col] = False
for row in range(m):
    for col in range(n):
        if not visited[row][col] and paper[row][col]:
            sizes.append(check_area(row,col))

print(len(sizes))

for size in sorted(sizes):
    print(size, end = " ")
print()



