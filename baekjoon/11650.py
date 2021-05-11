from sys import stdin 

locations = [tuple(map(int,stdin.readline().strip().split())) for _ in range(int(stdin.readline().strip()))]
locations.sort()

for i in locations:
    x,y = i
    print(f"{x} {y}")