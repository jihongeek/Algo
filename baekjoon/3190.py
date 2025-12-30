from sys import stdin

n = int(stdin.readline().strip())
board = [[-1]*n for _ in range(n)]

k = int(stdin.readline().strip())
for _ in range(k):
  row, column = map(int, stdin.readline().strip().split())
  board[row-1][column-1] = -2

head_row = 0
head_column = 0
board[0][0] = 1

tail_row = 0
tail_column = 0

l = int(stdin.readline().strip())
turn_info = [False]*10001

for _ in range(l):
  x, c = stdin.readline().strip().split()
  x = int(x)
  turn_info[x] = c



moves = [(-1,0),(0,1),(1,0),(0,-1)]
now_direction = 1

time_count = 1
while True:
    row_move, column_move = moves[now_direction]
    head_row,head_column = head_row + row_move, head_column + column_move
    if head_row >= n or head_row < 0 or head_column >= n or head_column < 0:
        break
    if board[head_row][head_column] >= 0:
        break
    if board[head_row][head_column] == -1:
       row_move,column_move = moves[board[tail_row][tail_column]]
       board[tail_row][tail_column] = -1
       tail_row,tail_column = tail_row + row_move, tail_column + column_move
    if turn_info[time_count] == "L":
        now_direction = (4 + (now_direction - 1)) % 4
    if turn_info[time_count] == "D":
        now_direction = (now_direction + 1) % 4
    board[head_row][head_column] = now_direction
    time_count += 1
print(time_count)   