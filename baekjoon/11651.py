from sys import stdin
from operator import itemgetter
n = int(stdin.readline().strip())
locations = [ tuple(map(int, stdin.readline().strip().split())) for _ in range(n)]

locations = sorted(locations,key=itemgetter(1,0))
for location in locations:
    print(f"{location[0]} {location[1]}")