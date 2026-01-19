from sys import stdin 

t = int(stdin.readline().strip())
for _ in range(t):
  dp = [1] * 10001
  n = int(stdin.readline().strip())
  for j in [2,3]:
      for i in range(j,n+1):
        dp[i] = dp[i] + dp[i - j]
  print(dp[n])      
      
