from sys import stdin

sumOfTime = 0
n = stdin.readline().strip()
peoples = list(map(int,stdin.readline().strip().split()))
peoples.sort()

for i in range(len(peoples)):
    sumOfTime += sum(peoples[:i+1])
print(sumOfTime)
