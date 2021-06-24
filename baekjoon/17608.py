from sys import stdin
numOfSticks = int(stdin.readline().strip())
sticks = list(reversed([ int(stdin.readline().strip()) for _ in range(numOfSticks)]))
count = 1
nowMax = sticks[0]
for i in sticks:
    if i > nowMax:
        count+=1
        nowMax = i
print(count)
