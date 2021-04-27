from sys import stdin

n = int(stdin.readline().strip())
sides = [0]*81
sides[0] = 1
sides[1] = 1

for i in range(2,n+1):
    sides[i] = sides[i-1] + sides[i-2]
print(2*(sides[n-1]+sides[n]))
