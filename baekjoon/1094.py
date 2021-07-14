from sys import stdin

sticks = [64]
x = int(stdin.readline().strip())

while sum(sticks) > x:
    sticks[-1] = sticks[-1]//2
    sticks.append(sticks[-1]) 
    if sum(sticks[:-1]) >= x:
        sticks.pop()
print(len(sticks))