import sys

def getvalue(x):
    return x[1]

scores = {}

for i in range(8):
    scores[i+1] = int(sys.stdin.readline().strip())

scores = sorted(scores.items(),key=getvalue)
scorelist = []
scorenum = []
for i in range(3,8):
    scorenum.append(scores[i][0])
    scorelist.append(scores[i][1])
print(sum(scorelist))
scorenum = sorted(scorenum)
for i in scorenum:
    print(i, end= " ")