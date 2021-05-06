from sys import stdin,setrecursionlimit
setrecursionlimit(1000000)
memo = dict()
def findMin(n):
    if n in memo:
        return memo[n]
    if n == 1:
        memo[1] = 0
        return memo[1]
    else:
        minCase = 1000001
        if n % 3 == 0:
            minCase = min(findMin(n//3),minCase)
        if n % 2 == 0:
            minCase = min(findMin(n//2),minCase)
        minCase = min(findMin(n-1),minCase)
    memo[n] = 1+ minCase
    return memo[n]
print(findMin(int(stdin.readline().strip())))