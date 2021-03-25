from sys import stdin

n,kim,lim = map(int,stdin.readline().strip().split())
count = 1
while True:
    if abs(kim-lim) == 1:
        if kim % 2 == 0 and kim//2 == (lim + 1)//2:
            break
        elif lim % 2 == 0 and lim //2 == (kim + 1)//2:
            break
    count += 1
    if kim % 2 == 0:
        kim //= 2
    else:
        kim = (kim+1) // 2
    if lim % 2 == 0:
        lim //= 2
    else:
        lim = (lim+1) // 2
print(count)







