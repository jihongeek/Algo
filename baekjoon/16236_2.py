from sys import stdin
from collections import deque
import heapq

n = int(stdin.readline().strip())


board = []

ate_fishes = -1
shark_size = 2
time_sum = 0

shark_location = (0,0)

for _ in range(n):
  line = stdin.readline().strip().split()
  board.append(list(map(int,line)))
for row in range(n):
  for col in range(n):
    if board[row][col] == 9:
      shark_location = (row,col)
      board[row][col] = 0

ediable_heap = [(0,shark_location[0], shark_location[1])]
heapq.heapify(ediable_heap)

moves = [(1,0),(0,1),(-1,0),(0,-1)]

def isEdible(row,col,shark_size): 
  global n,board
  if row < 0 or row >= n or col < 0 or col >= n:
    return False
  if board[row][col] == 0 or board[row][col] >= shark_size:
    return False
  return True

def isMovable(row,col,shark_size):
  global n,board
  if row < 0 or row >= n or col < 0 or col >= n:
    return False
  if board[row][col] > shark_size:
    return False
  return True

def findEdibleFishes(row,col):
  global visited,ate_fishes, shark_size, ediable_heap
  q = deque([(0,row,col)])
  visited[row][col] = True  
  while q:
    distance,row,col = q.popleft()
    for move in moves:
      row_move,col_move = move
      next_row = row + row_move
      next_col = col + col_move
      if (isEdible(next_row,next_col,shark_size) and visited[next_row][next_col] == False):
        heapq.heappush(ediable_heap,(distance+1,next_row,next_col))
        visited[next_row][next_col] = True
      elif (isMovable(next_row,next_col,shark_size) and visited[next_row][next_col] == False):
      
        q.append((distance+1,next_row,next_col))
        visited[next_row][next_col] = True

while len(ediable_heap) > 0:
  distance, row, col = heapq.heappop(ediable_heap)
  ediable_heap = []
  heapq.heapify(ediable_heap)
  time_sum += distance
  board[row][col] = 0
  ate_fishes += 1
  if ate_fishes == shark_size:
    ate_fishes = 0
    shark_size += 1

  visited = [[False] * n for _ in range(n)]
  findEdibleFishes(row,col)

print(time_sum)


