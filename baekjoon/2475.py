from sys import stdin
print(sum([ int(x)**2 for x in stdin.readline().strip().split()])%10)
