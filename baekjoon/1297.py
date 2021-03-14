from sys import stdin
from math import sqrt
diagonal, heightRatio, widthRatio = map(int, stdin.readline().strip().split())

height = int(diagonal * heightRatio / sqrt(heightRatio**2 + widthRatio**2))  
width = int(diagonal * widthRatio / sqrt(heightRatio**2 + widthRatio**2))  
print(f"{height} {width}")