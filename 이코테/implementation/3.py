from sys import stdin 
"""
문제 설명 : N*M of 1*1, 칸은 육지 또는 바다, 캐릭터 동서남북 바라봄 

움직임 룰 
캐릭터 왼쪽 방향 아직 가보지 않은 칸 있으면 왼쪽 회전 한다음 한칸 전진, 가봤다면 회전만, 다시 왼쪽확인
네 방향 모두 가본 칸 또는 바다 일 경우 : 방향 유지한 채 뒤로 가는데 이때도 만약에 바다인 경우에 멈추기

칸의 좌표와 방향이 주어짐
방행은 0(북), 1(동), 2(남), 3(서)

전략 :
왼쪽 회전 -> (4(요수 갯수) + d(현재) - 1) % 4(요소갯수)
4 + 0 - 1 % 4 = 3 북 -> 서
4 + 1 - 1 % 4 = 0 동 -> 북
4 + 2 - 1 % 4 = 1 남 -> 동
4 + 3 - 1 % 4 = 2 서 -> 남

방문한 칸과, 맵 데이터(0:육지, 1:바다)를 n*m 배열에 저장하기
설명대로 좌표를 움직일때 방문한 칸의 수를 출력하기
음 현재 방향 기준에서 어떻게 왼쪽 방향을 판단하지 위치를? -> 대칭이동을 생각해야하나?

왼쪽과 뒤 방향만 생각하면됨 : 왼쪽은 
북 : b - 1
동 : a - 1
서 : a + 1
남 : b + 1

뒤쪽은 

북 : a + 1
동 : b + 1
서 : b - 1
남 : a - 1

"""



n,m = map(int, stdin.readline().strip().split())
a,b,d = map(int,stdin.readline().strip().split())

# a,b = a - 1, b -1
map_data = [stdin.readline().strip().split() for _ in range(m)]
visited = [ [False] * m for _ in range(n) ]

left_moves = [(0,-1), (-1,0), (0,1), (1,0)]
back_moves = [(1,0),(0,1), (-1,0), (0,-1)]

def is_in_map(a,b, n,m):
  if not (a >= 0 and a < n and b >= 0 and b < m):
    return False
  return True

def check_direction_visitable(a,b):
  moves = [(-1,0),(-1,0),(0,1),(0,-1)] 
  for move in moves:
    row_move, column_move = move
    if is_in_map(a + row_move, b + column_move,n,m) and map_data[a+ row_move][b+column_move] != "1" and not visited[a+ row_move][b+column_move]:
      return True
  return False
count = 0
visited[a][b] = True
while True:
  
  left_row_move, left_column_move = left_moves[d]
  back_row_move, back_column_move = back_moves[d]
  lefted_a, lefted_b = a + left_row_move, b + left_column_move
  backed_a, backed_b = a + back_row_move, b + back_column_move
  
  if is_in_map(lefted_a,lefted_b,n,m) and not visited[lefted_a][lefted_b] and map_data[lefted_a][lefted_b] != "1":
    d = (4+d-1) % 4
    a,b = lefted_a, lefted_b
    print(a,b,d,"왼쪽 턴 및 이동한 케이스")
    continue
  if is_in_map(lefted_a,lefted_b,n,m) and (visited[lefted_a][lefted_b] or map_data[lefted_a][lefted_b] == "1"):
    d = (4+d-1) % 4
    print(a,b,d,"왼쪽 턴만 한 케이스")
  if is_in_map(backed_a,backed_b,n,m) and not check_direction_visitable(a,b) and map_data[backed_a][backed_b] != "1":
    a,b = backed_a,backed_b
    print(a,b,d,"뒤로간 케이스")
    continue
  if is_in_map(backed_a,backed_b,n,m) and not check_direction_visitable(a,b) and map_data[backed_a][backed_b] == "1":
    break

for visited_line in visited:
  for visit in visited_line:
    if visit:
      count += 1
print(count)