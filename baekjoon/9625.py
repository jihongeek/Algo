from sys import stdin

dp = [(0,1),(1,1)]
n = int(stdin.readline().strip())
for i in range(2,n):
    a = dp[i-1][1]
    b = dp[i-1][0] + dp[i-1][1]
    dp.append((a,b))
    
print(f"{dp[n-1][0]} {dp[n-1][1]}")