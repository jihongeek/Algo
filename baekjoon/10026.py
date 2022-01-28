from sys import stdin 
from collections import deque

"""
    전략: 
        BFS를 2번 진행해 색깔 별 구역을 찾는다.
        1) 적록색약이 아닌 경우 -> 상하좌우 칸의 색이 같을 경우에만 진행
        2) 적록색약이 아닌경우 -> 상하좌우 칸의 색이 서로 R,G일 경우와 B일 경우에만 진행 
        2의 문제를 해결하기 위해 이미 방문했던 칸인지 확인, 색약여부에 따라 진해할 수 있는 칸인지 확인하기  
"""

def isValid(row, col, new_row, new_col,color_weakness):
    # 그림안에 있는 칸인지 확인
    if not (0 <= new_row < n and 0 <= new_col < n):
        return False
    # 이미 방문했는 지 확인
    if visited[new_row][new_col]:
        return False
    # R,G or B -> 논리 연산을 통해 해결 할 수 있지 않을 까?
    # R G, G R -> (R == G or G == R)
    # 2칸의 색이 같으면 무조건 ok, 
    color = picture[row][col]
    new_color =  picture[new_row][new_col]
    
    # 색깔이 다르고, 적록색약이 아닐경우
    if color != new_color and not color_weakness:
        return False


    # 색깔이 다르고, 적록색약인 경우
    if color == "R" and new_color == "B" and color_weakness:
        return False
    if color == "B" and new_color == "R" and color_weakness:
        return False
    if color == "G" and new_color == "B" and color_weakness:
        return False
    if color == "B" and new_color == "G" and color_weakness:
        return False
    return True 

def count_area(row,col,color_weakness):
    """
        bfs를 이용해 각 구역 갯수를 세는 함수
    """
    q = deque()
    visited[row][col] == True
    count_dict[picture[row][col]] += 1
    q.append((row,col))

    while len(q) > 0:
        row,col = q.popleft()
        # 현재 위치에서 위쪽에 있는 칸이 같은 영역인지 확인
        if isValid(row,col,row-1,col,color_weakness):
            visited[row-1][col] = True 
            q.append((row-1,col))
        # 현재 위치에서 아래쪽에 있는 칸이 같은 영역인지 확인
        if isValid(row,col,row+1,col,color_weakness):
            visited[row+1][col] = True 
            q.append((row+1,col)) 
        # 현재 위치에서 왼쪽에 있는 칸이 같은 영역인지 확인
        if isValid(row,col,row,col-1,color_weakness):
            visited[row][col-1] = True 
            q.append((row,col-1))
        # 현재 위치에서 왼쪽에 있는 칸이 같은 영역인지 확인
        if isValid(row,col,row,col+1,color_weakness):
            visited[row][col+1] = True 
            q.append((row,col+1))
         

count_dict = {
    "R" : 0,
    "G" : 0,
    "B" : 0
}
n = int(stdin.readline().strip())
picture = [stdin.readline().strip() for _ in range(n)]
visited = [[False]*n for _ in range(n)]

for row in range(n):
    for col in range(n):
        if not visited[row][col]:
            count_area(row,col,False)
print(count_dict["R"] + count_dict["G"] + count_dict["B"], end= " ")

count_dict = {
    "R" : 0,
    "G" : 0,
    "B" : 0
}
visited = [[False]*n for _ in range(n)]
for row in range(n):
    for col in range(n):
        if not visited[row][col]:
            count_area(row,col,True)
print(count_dict["R"] + count_dict["G"] + count_dict["B"], end= " ")



    
        
                
        

