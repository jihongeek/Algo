from sys import stdin 
nums = list(map(int,stdin.readline().strip().split()))

for i in range(min(nums),1000001):
    count = 0
    for j in nums:
        if i%j == 0:
            count += 1
    if count >= 3:
        print(i)
        break
