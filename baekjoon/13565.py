from sys import stdin
from collections import deque
"""
    bfs를 통해서 전류의 전달을 구현하고 
    만약 안쪽까지 전달(전달된 전류 좌표의 행 ==  m) 되었다면 YES
    아니면 NO 
"""

def is_flowable(row:int,col:int):
    """ 
        전류가 전달될 수 있는 지 확인 하는 함수
    """
    if not (0 <= row < m and 0 <= col < n):
        return False
    if fabric[row][col] != "0":
        return False
    if flown[row][col] == True:
        return False
    return True
     
def flow(row:int,col:int):
    """
        너비 우선 탐색을 통해 전류의 전달을 구현하는 함수
    """
    flown[row][col] = True
    q = deque()
    q.append((row,col))
    while len(q) > 0:
        now_row,now_col = q.popleft()
        # 위쪽으로 전달 가능할 경우 전달
        if is_flowable(now_row-1,now_col):
            flown[now_row-1][now_col] = True
            q.append((now_row-1,now_col))
        # 아래쪽으로 전달 가능할 경우 전달
        if is_flowable(now_row+1,now_col):
            flown[now_row+1][now_col] = True
            q.append((now_row+1,now_col))
        # 왼쪽으로 전달 가능할 경우 전달
        if is_flowable(now_row,now_col-1):
            flown[now_row][now_col-1] = True
            q.append((now_row,now_col-1))
        # 오른쪽으로 전달 가능할 경우 전달
        if is_flowable(now_row,now_col+1):
            flown[now_row][now_col+1] = True
            q.append((now_row,now_col+1))
    
m,n = map(int,stdin.readline().strip().split())

flown = [[False]*n for _ in range(m)]
fabric = []
for _ in range(m):
    line = stdin.readline().strip()
    fabric.append(line)
    

# 바깥 쪽에서 전류의 전달 진행
for col in range(n):
    if fabric[0][col] == "0" and not flown[0][col]:
        flow(0,col)
# 침투 여부를 flown 배열로 확인
percolatability = False 
for col in range(n):
    if flown[m-1][col] == True:
        percolatability = True
        break
# 침투 여부에 따른 값 출력
if percolatability == True:
    print("YES")
else:
    print("NO")

