N  = input()
originalN = N
cycle = 0
if int(originalN) < 10:
    N = "0%s"%str(originalN[-1])
while True:
    N = N[-1] + str(int(N[0])+int(N[-1]))[-1]
    cycle = cycle  +1
    if N == "0"+originalN:
        break
    elif N == originalN:
        break
print(cycle,end="")
        
