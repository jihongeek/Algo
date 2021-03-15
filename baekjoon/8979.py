from sys import stdin
from operator import itemgetter
n , k = map(int,stdin.readline().strip().split()) 
medalOfNations = [list(map(int,stdin.readline().strip().split())) for _ in range(n)]

medalOfNations = sorted(medalOfNations,key=itemgetter(1,2,3),reverse=True)
medalOfNations[0] = medalOfNations[0] + [1]
sameCount = 0
for i in range(1,n):
    if medalOfNations[i][1:4] == medalOfNations[i-1][1:4]:
        medalOfNations[i] = medalOfNations[i] + [medalOfNations[i-1][4]]
        sameCount += 1
    else:
        medalOfNations[i] = medalOfNations[i] + [medalOfNations[i-1][4] + sameCount + 1]
        sameCount = 0

for i in medalOfNations:
    if i[0] == k:
        print(i[4])
        break