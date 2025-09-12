from sys import stdin
"""
문제 설명 : 나이트가 움직일 수 있는 모든 경우의 수 구하기

전략 : 현재 나이트 위치에서 모든 방향에서 이동할 때 8*8 좌표 평면에서 나가는 경우 제외하고 경우의 수 구하기
"""

moves = [(-2,1), (-2,-1), (2,1),(2,-1), (1, -2), (-1,-2), (1,2),(-1,2)]

knight_location_input = stdin.readline().strip()
knight_location = (ord(knight_location_input[0]) - ord("a") + 1, int(knight_location_input[1]))
count = 0
for move in moves:
    row_move,column_move = move
    if  knight_location[0] + row_move < 1:
        continue
    if  knight_location[0] + row_move > 8:
        continue
    if  knight_location[1] + column_move > 8:
        continue
    if  knight_location[1] + column_move < 1:
        continue
    count += 1
print(count)