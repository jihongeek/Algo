from sys import stdin
now = 1
count = 1
numToPlus = 2
s = int(stdin.readline().strip())
while now != s:
    if now + numToPlus > s:
        now += 1
        numToPlus += 2
        continue
    now+=numToPlus
    numToPlus+=1
    count += 1 
print(count)