from sys import stdin

maxWeight = -1
n = int(stdin.readline().strip())
ropes = sorted([int(stdin.readline().strip()) for _ in range(n)])
for i in range(n):
    maxWeight = max(maxWeight, ropes[i]*(n-i))
print(maxWeight)
         
