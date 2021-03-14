import math

sum = 0
perfectsqrs = []


m = int(input())
n = int(input())

for i in range(m,n+1):
    isqrt = math.sqrt(i)  
    if int(isqrt) == isqrt and isqrt ** 2 == i:
        sum = sum + i
        perfectsqrs.append(i)
if sum == 0:
    print(-1)
else:
    print(sum)
    print(perfectsqrs[0])
