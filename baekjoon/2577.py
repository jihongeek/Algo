inputlist = []
countlist = [0,0,0,0,0,0,0,0,0,0]
for i in range(3):
    inputlist.append(int(input()))
resultlist = str(inputlist[0]*inputlist[1]*inputlist[2])
for i in range(10):
    for j in resultlist:
        if i == int(j):
            countlist[i]=countlist[i]+1
for i in countlist:
    print(i)
    


