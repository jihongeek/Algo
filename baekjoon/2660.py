from sys import stdin

n = int(stdin.readline().strip())
memberMatrix = [[0]*n for _ in range(5)]

while True:
    a, b = map(int, stdin.readline().strip().split())
    if a == -1 and b == -1:
        break
    memberMatrix[a-1][b-1] = 1
    memberMatrix[b-1][a-1] = 1

for i in range(n):
    for j in range(n):
        if i != j and memberMatrix[i][j] == 1:
            for k in range(n):
                if k != i and j!=k and memberMatrix[j][k] > 0:
                    if memberMatrix[i][k] == 0:
                        memberMatrix[i][k] = memberMatrix[j][k] + 1
                        memberMatrix[k][i] = memberMatrix[i][k]
                    else:
                        memberMatrix[i][k] = min(memberMatrix[j][k] + 1, memberMatrix[i][k])
                        memberMatrix[k][i] = memberMatrix[i][k]
                        
minScore = 51
candidates = []
for realation in memberMatrix:
    minScore = min(max(realation), minScore)

for i in range(len(memberMatrix)):
    if max(memberMatrix[i]) == minScore:
        candidates.append(i)

print(minScore, len(candidates))

for i in candidates:
    print(i+1, end=" ")
