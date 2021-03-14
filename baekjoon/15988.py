from sys import stdin

testcase = int(input())
dp = [0]*(1000001)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for j in range(4,1000001):
        dp[j] = dp[j-1]%1000000009 + dp[j-2]%1000000009 + dp[j-3]%1000000009

for i in range(testcase):
    n = int(stdin.readline().strip())
    print(dp[n]%1000000009)


         
