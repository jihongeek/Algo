from sys import stdin

n = int(stdin.readline().strip())
stairs = [ int(stdin.readline().strip()) for _ in range(n)]
dp = [[0]*2 for _ in range(n)]
for i in range(n):
    if i == 0:
        dp[0][0],dp[0][1] = stairs[0],stairs[0]
    elif i == 1:
        dp[1][0],dp[1][1] = stairs[1],stairs[0]+stairs[1]
    else:
        dp[i][0],dp[i][1] = max(dp[i-2][0],dp[i-2][1])+stairs[i], dp[i-1][0]+stairs[i]
print(max(dp[n-1]))
