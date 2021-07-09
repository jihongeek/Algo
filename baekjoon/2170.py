from sys import stdin 
n = int(stdin.readline().strip())
lines = [tuple(map(int,stdin.readline().strip().split())) for _ in range(n)]
lines.sort()
sumOfLines = lines[0][1] - lines[0][0]  
for i in range(1,n):
    if lines[i][0] < lines[i-1][1]:
        if lines[i][1] < lines[i-1][1]:
            continue
        sumOfLines += abs(lines[i][1] - lines[i-1][1])
    else:
        sumOfLines += abs(lines[i][1] - lines[i][0])
print(sumOfLines)