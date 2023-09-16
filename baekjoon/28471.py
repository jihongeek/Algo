from sys import stdin
from collections import deque

"""
    전략 : 시작가능한 칸(#)마다 bfs를 실시해서 목적지(F)에 도착가능하면 카운트 세기 -> 이렇게 하면 2000^3 이기에 시간초과!!
    따라서 반대로 생각해서(목적지에서 아래로 못감) 목적지(F)에서 빈공간으로 bfs를 실시해서 빈공간마다 카운트 세기  
"""
moves = [(-1,-1), (-1,1), (0,-1), (0,1), (1,1), (-1,0), (1,-1)] 

def is_visitable(row,col):
    if not (0 <= row < n and 0 <= col < n):
        return False
    if visited[row][col] is True:
        return False
    if board[row][col] == "#":
        return False
    return True

def visit(start_row,start_col):
    global count,visited
    q = deque()
    visited[start_row][start_col] = True
    q.append((start_row,start_col))
    while len(q) > 0:
        last_row,last_col = q.popleft()
        if board[last_row][last_col] == ".":
            count += 1
        for move in moves:
            row_move,col_move = move
            next_row = last_row + row_move
            next_col = last_col + col_move
            if is_visitable(next_row,next_col) is True:
                visited[next_row][next_col] = True
                q.append((next_row,next_col))
            
count = 0 
n = int(stdin.readline().strip())
visited = [ [False]*n for _ in range(n) ]

board = []
for _ in range(n):
    board.append(stdin.readline().strip())

for row in range(n):
    for col in range(n):
        if board[row][col] == "F":
            visit(row,col)
            visited = [ [False]*n for _ in range(n) ]
print(count)