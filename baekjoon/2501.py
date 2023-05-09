from sys import stdin

n,k = map(int, stdin.readline().strip().split())
count = 0
last_divisor = 0
for i in range(1,n+1):
    if n % i == 0:
        last_divisor = i
        count += 1
    if count == k:
        break
if count < k:
    last_divisor = 0
print(last_divisor)