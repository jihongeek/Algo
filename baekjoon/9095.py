from sys import stdin 

def findCase(n):
    if n == 0:
        return 1
    result = 0
    if n >= 1:
        result += findCase(n-1)
    if n >= 2:
        result += findCase(n-2)
    if n >= 3:
        result += findCase(n-3)
    return result

n = int(stdin.readline().strip())
for _ in range(n):
    print(findCase(int(stdin.readline().strip())))