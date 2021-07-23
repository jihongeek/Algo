from sys import stdin 
n = int(stdin.readline().strip())
locations = [ tuple(map(int, stdin.readline().strip().split())) for _ in range(n)]
paper = [[False]*100 for _ in range(100)]
iOverlaped = 0
for location in locations:
    for row in range(location[1],10+location[1]):
        for col in range(location[0],10+location[0]):
            paper[row][col] =True
count = 0
for i in range(100):
    for j in range(100):
        if paper[i][j]:
            count += 1
print(count)