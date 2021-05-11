from sys import stdin
n = int(stdin.readline().strip())
dp = [0]*(n+1)
for i in range(1,n+1):
    if i == 1:
        dp[1] = 0
        continue
    minCase = 1000001
    if i % 3 == 0:
        minCase = min(dp[i//3],minCase)
    if i % 2 == 0:
        minCase = min(dp[i//2],minCase)
    minCase = min(dp[i-1],minCase)
    dp[i] = 1 + minCase
print(dp[n])
            
