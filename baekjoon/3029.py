from sys import stdin
nowTime = list(map(int,stdin.readline().strip().split(":")))
explosionTime =list(map(int,stdin.readline().strip().split(":")))
waitTime = [0,0,0]
borrowedCarries = 0

"""
    내림수를 이용한 시간 차를 이용한 풀이
"""

for i in range(2,-1,-1):
    carry = 0
    if borrowedCarries > 0:
        carry = 1
        borrowedCarries -= 1
    if explosionTime[i] - nowTime[i] - carry >= 0:
        waitTime[i] += (explosionTime[i] - nowTime[i] - carry)
    else: 
        borrowedCarries += 1
        if i > 0:
            waitTime[i] += (explosionTime[i]+60 - nowTime[i] - carry)
        else:
            waitTime[i] += (explosionTime[i]+24 - nowTime[i]- carry)
if nowTime == explosionTime:
    waitTime = [24,0,0]
waitTime = list(map(lambda x : "%02d"%x ,waitTime))
print(":".join(waitTime))


