from sys import stdin

t = int(stdin.readline().strip())

for _ in range(t):
    n,m = map(int,stdin.readline().strip().split())
    count = 0
    for i in range(n,m+1):
        count += str(i).count("0")
    print(count)
    