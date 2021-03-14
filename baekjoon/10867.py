import sys

n = int(sys.stdin.readline().strip())
inputnums = map(int,sys.stdin.readline().strip().split())
inputnums = sorted(list(set(inputnums)))

for i in inputnums:
    print(i, end=" ")
