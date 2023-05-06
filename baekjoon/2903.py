from sys import stdin

start = 2
for _ in range(int(stdin.readline().strip())):
    start = start*2 - 1
print(start**2)