from sys import stdin

n = int(stdin.readline().strip())
students = [ list(map(int,stdin.readline().strip().split())) for _ in range(n)]
winners = []
winnersCountry = [0]*n
for i in range(n):
    for j in range(n-1):
        if students[j+1][2] > students[j][2]:
            students[j+1],students[j] = students[j],students[j+1]
for i in students:
    if len(winners) == 3:
        break
    if winnersCountry[i[0]-1] > 1:
        continue
    else:
        winners.append(i)
        winnersCountry[i[0]-1] += 1

for i in winners:
    print(f"{i[0]} {i[1]}")
