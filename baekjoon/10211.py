from sys import stdin

testcase = int(stdin.readline().strip())

for _ in range(testcase):
    n = int(stdin.readline().strip())
    array = list(map(int,stdin.readline().strip().split()))
    dp = [0]*n
    dp[0] = array[0]
    for i in range(1,n):
        # 점화식
        dp[i] = max(dp[i-1] + array[i], array[i])
    print(max(dp))
    