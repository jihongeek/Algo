from sys import stdin
from collections import deque

EMPTY, SNAKE, APPLE =  (0, 1, 2)

n = int(stdin.readline().strip())

board = [ [0]*(n+1) for _ in range(n+1) ]
k = int(stdin.readline().strip())

for _ in range(k):
  row,col = map(int, stdin.readline().strip().split())
  board[row][col] = APPLE

turns = [False] * 10000
direction = 0
moves = [(0,1),(1,0),(0,-1),(-1,0)]
l = int(stdin.readline().strip())

for _ in range(l):
  time, turn = stdin.readline().strip().split()
  turns[int(time)] = turn 


time = 1
snake = deque([(1,1)])
board[1][1] = SNAKE

while True:
  head_row,head_col = snake[-1]
  row_move,col_move = moves[direction]
  next_row, next_col = (head_row + row_move, head_col + col_move)
  if next_row <= 0 or next_row > n or next_col <=0 or next_col > n:
    break 
  if board[next_row][next_col] == SNAKE:
    break
  if board[next_row][next_col] != APPLE:
    tail_row, tail_col = snake.popleft()
    board[tail_row][tail_col] = EMPTY
  snake.append((next_row,next_col))
  board[next_row][next_col] = SNAKE
  if turns[time] == "L":
    direction = (direction - 1) % 4
  if turns[time] == "D":
    direction = (direction + 1) % 4
  time += 1

print(time)



