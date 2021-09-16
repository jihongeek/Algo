from sys import stdin

n = int(stdin.readline().strip())
numList = [0]*201

for num in list(map(int,stdin.readline().strip().split())):
    numList[num+100] += 1
print(numList[int(stdin.readline().strip())+100])  