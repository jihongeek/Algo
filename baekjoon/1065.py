def isHansu(n):
    if n <10:
        return True
    else:
        oseries = list(map(int,str(n)))
        pseries = [int(str(n)[0])]
        d = int(str(n)[1]) - int(str(n)[0])
        for i in range(len(oseries)):
            if i == len(oseries)-1:
                break
            pseries.append(oseries[i]+d)
        if oseries == pseries:
            return True
        else:
            return False
hansues = []
for i in range(1,int(input())+1):
    if isHansu(i) == True:
        hansues.append(i)
print(len(hansues))