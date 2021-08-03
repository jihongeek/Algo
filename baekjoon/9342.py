from sys import stdin
from re import fullmatch

for i in range(int(stdin.readline().strip())):
    if fullmatch("[A-F]{0,1}A+F+C+[A-F]{0,1}",stdin.readline().strip()):
        print("Infected!")
    else:
        print("Good")