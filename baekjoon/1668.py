from sys import stdin

n = int(stdin.readline().strip())
trophies = [int(stdin.readline().strip()) for _ in range(n)]
trophiesReversed = list(reversed(trophies))
maxNow = 0
left = 1
right = 1
maxNowleft = trophies[0] 
maxNowRight = trophiesReversed[0] 
for i in range(1,n):
    if maxNowleft < trophies[i]:
        left += 1
        maxNowleft = trophies[i]
    if maxNowRight < trophiesReversed[i]:
        right += 1
        maxNowRight = trophiesReversed[i]

print(left)
print(right)