n = int(input())
minOfPack = 10000
for i in range(n):
    for j in range(n):
        if 3*i + 5*j > n:
            break
        elif 3*i + 5*j == n:
            minOfPack = min(i+j,minOfPack)
if minOfPack == 10000:
    print(-1)
else:
    print(minOfPack)
