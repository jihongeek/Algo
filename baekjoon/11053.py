from sys import stdin
n = int(stdin.readline().strip())
series = list(map(int,stdin.readline().strip().split()))
dp = [1]*n
for i in range(n):
    for j in range(i):
        if series[i] > series[j]:
            dp[i] = max(dp[j] + 1,dp[i])
print(max(dp))