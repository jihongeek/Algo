from sys import stdin

now_location = (1,1)
n = int(stdin.readline().strip())
moving_plan = stdin.readline().strip().split()

for move in moving_plan:
  now_row, now_column = now_location
  if move == "R" and now_column + 1 <= n:
    now_location = (now_row, now_column + 1)
    continue
  if move == "L" and now_column - 1 >= 1:
    now_location = (now_row, now_column - 1)
    continue
  if move == "U" and now_row - 1 >= 1:
    now_location = (now_row-1, now_column)
    continue
  if move == "D" and now_row + 1 <= n:
    now_location = (now_row + 1, now_column)

print(" ".join(map(str,now_location)))
