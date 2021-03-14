from sys import stdin
import heapq
testcase = int(stdin.readline().strip())

for t in range(testcase):
    money = 1
    que = []
    n = int(stdin.readline().strip())
    slimes = list(map(int, stdin.readline().strip().split()))
    for i in range(n):
            heapq.heappush(que,slimes[i])
    while (len(que) > 1):
        nowEnergy = heapq.heappop(que) * heapq.heappop(que)
        money = (money * nowEnergy)%1000000007
        heapq.heappush(que,nowEnergy)
    print(money%1000000007)

