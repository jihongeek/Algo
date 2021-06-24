from sys import stdin

factorial = 1
count = 0
n = int(stdin.readline().strip())
for i in range(2,n+1):
    factorial = factorial * i

while factorial > 0:
    if factorial % 10 != 0:
        break
    factorial = factorial // 10
    count+=1
print(count)