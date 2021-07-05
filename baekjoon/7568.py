from sys import stdin 
n = int(stdin.readline().strip())
people = [tuple(map(int,stdin.readline().strip().split())) for _ in range(n)]

for i in range(n):
    count = 0
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count += 1
    print(count+1,end=" ")