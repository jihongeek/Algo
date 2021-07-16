from sys import stdin

n = int(stdin.readline().strip())
dp = [0]*n

for i in range(n):
    if i + 1 == 1:
        dp[i] = 1
    elif i + 1 == 2:
        dp[i] = 3
    else:
        dp[i] = 2*dp[i-2] + dp[i-1]

print(dp[-1]%10007)