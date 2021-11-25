from sys import stdin 

n = int(stdin.readline().strip())

triangle = []
dp = [[0]*n for _ in range(n)]

for _ in range(n):
    triangle.append(list(map(int,stdin.readline().strip().split())))
dp[0][0] = triangle[0][0]
for i in range(0,n-1):
    for j in range(0,i+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j]+triangle[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])
print(max(dp[n-1]))