from sys import stdin

w = sorted([ int(stdin.readline().strip()) for _ in range(10) ])
k = sorted([ int(stdin.readline().strip()) for _ in range(10) ])
print(f"{w[-1]+w[-2]+w[-3]} {k[-1]+k[-2]+k[-3]}")