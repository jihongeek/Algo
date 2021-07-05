for i in range(2992,10000):
    toDivided = i
    sums = [0]*3
    while toDivided > 0:
        sums[0] = sums[0] + (toDivided % 10)
        toDivided //= 10
    
    toDivided = i
    while toDivided > 0:
        sums[1] = sums[1] + (toDivided % 12)
        toDivided //= 12
    
    toDivided = i
    while toDivided > 0:
        sums[2] = sums[2] + (toDivided % 16)
        toDivided //= 16
    
    if sums[0] == sums[1] == sums[2]:
        print(i)
        