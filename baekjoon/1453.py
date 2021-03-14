runnum = int(input())
cnt = 0
inputnums = input().split()
for i,j in enumerate(inputnums):
    if j in inputnums[i+1:]:
        cnt = cnt + 1 
print(cnt)