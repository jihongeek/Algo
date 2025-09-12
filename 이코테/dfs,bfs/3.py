from sys import stdin 

"""
얼음 틀의 모양이 주어졌을 때 아이스크림 갯수 구하기
(상하좌우 붙어있는 경우만 1개로 침)구멍이 뚤린 부분 0, 칸막이 1

dfs로 돌면서 아이스크림 갯수 구하기

방문 표시 n*m 배열 만들기
얼음 틀을 n*m 인접 행렬로 이뤄진 그래프로 나타내기 

전략: 각칸을 방문하지 않았으면 방문하고 카운트 1 증가, 상하좌우 인접한 칸이 방문 가능하면 방문
방문가능한 칸이 없을 때 까지 재귀호출
"""
n,m = map(int, stdin.readline().strip().split())
ice_board = [stdin.readline().strip() for _ in range(n)]
visited = [[False]*m for _ in range(n)]
moves = [(1,0),(-1,0),(0,-1),(0,1)]

count = 0

def dfs(row,column):
  global visited, ice_board
  visited[row][column] = True
  for move in moves:
    row_move, column_move = move
    if row + row_move < 0 or row + row_move >= n:
      continue  
    if column + column_move < 0 or column + column_move >= m:
      continue 
    if visited[row+row_move][column + column_move] or ice_board[row+row_move][column + column_move] == "1":
      continue
    dfs(row+row_move, column+column_move)
for row in range(n):
  for column in range(m):
    if not visited[row][column] and ice_board[row][column] == "0":
      dfs(row,column)
      count += 1
print(count)
