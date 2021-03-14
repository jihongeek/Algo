from sys import stdin

forbid = [[False]*201 for _ in range(201)] 
n,m = map(int,stdin.readline().strip().split())
count = 0
for i in range(m):
    icecream1,icecream2 = map(int, stdin.readline().strip().split())
    forbid[icecream1][icecream2] = True
    forbid[icecream2][icecream1] = True

for i in range(1,n+1):
    for j in range(1,n+1):
        if j == i:
            continue
        elif forbid[i][j] :
            continue
        for k in range(1,n+1):
            if k == i or k == j:
                continue
            elif forbid[j][k] or forbid[i][k]:
                continue
            else:
                count+=1 
print(count//6)
        
