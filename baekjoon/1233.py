from sys import stdin


s1,s2,s3 = map(int,stdin.readline().strip().split())
cases = [0]*(s1+s2+s3)
maxOfCases = -1
indexOfmax = 0
for i in range(1,s1+1):
    for j in range(1,s2+1):
        for k in range(1,s3+1):
            cases[i+j+k-3] += 1
for i,j in enumerate(cases):
    if j > maxOfCases:
        maxOfCases = j
        indexOfmax = i
print(indexOfmax+3)

