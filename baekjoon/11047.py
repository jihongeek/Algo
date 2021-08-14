from sys import stdin

n,k = map(int,stdin.readline().strip().split())
coins = [ int(stdin.readline().strip()) for _ in range(n)]
changes = [0]*n
changes[n-1] = k%coins[n-1]
coinNum = k//coins[n-1]
for i in range(n-2,-1,-1):
    coinNum += (changes[i+1]//coins[i])
    changes[i] = changes[i+1]%coins[i]
print(coinNum) 

