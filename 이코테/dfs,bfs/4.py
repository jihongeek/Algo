from sys import stdin
from collections import deque
"""
n*m 미로를 탈출 초기위치는 1,1이고 출구는 n,m에 위치
괴물을 피해서 탈출할 수 있는 최소 칸의 갯수 구하기

전략: BFS하면 최단거리 큐에 좌표와 이동 수 집어 넣기 (단 시작, 마지막 칸도 포함하기)

이번에는 방문과 이동을 합쳐서 생각해보기
-> 방문했으면 괴물이 있다고 생각하기

"""

n,m = map(int, stdin.readline().strip().split())
maze = [list(stdin.readline().strip()) for _ in range(n)]

def bfs():
  maze[0][0] = "0"
  queue = deque([(0,0,1)])
  while len(queue) > 0:
    row,column,count = queue.popleft()
    if row == n - 1 and column == m - 1:
      return count
    for move in [(0,1),(0,-1),(1,0),(-1,0)]:
      row_move,column_move = move
      new_row, new_column = row + row_move, column + column_move
      if new_row < 0 or new_row == n or new_column < 0 or new_column == m:
        continue
      if maze[new_row][new_column] == "0":
        continue
      maze[new_row][new_column] = "0"
      queue.append((new_row,new_column,count+1))
    
print(bfs())