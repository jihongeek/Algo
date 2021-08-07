from sys import stdin

board = [stdin.readline().strip() for _ in range(8)]
count = 0
for i in range(8):
    for j in range(i%2,8,2):
        if board[i][j] == "F":
            count += 1 
print(count)