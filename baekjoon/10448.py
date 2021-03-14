from sys import stdin

testcase = int(stdin.readline().strip())
nums = [int(stdin.readline().strip()) for _ in range(testcase)]
isPossible = 0
triNum = [0]*50
for i in range(1,50):
    if i == 1:
        triNum[i] = i
    else:
        triNum[i] = triNum[i-1] + i


for num in nums:
    isPossible = 0
    for i in range(1,50):
        if num - triNum[i] <= 0:
            break
        if isPossible == 1:
            break
        for j in range(1,50):
            if num - triNum[i] - triNum[j] <= 0:
                break
            if num - triNum[i] - triNum[j] in triNum:
                isPossible = 1
                break
    print(isPossible)
