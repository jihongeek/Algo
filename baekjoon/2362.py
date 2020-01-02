inputlist =[]
for i in range(9):
    inputlist.append(int(input()))
maximum = int(inputlist[0])
for i in inputlist:
    if int(i) > maximum:
        maximum = int(i)
print("%d"%(maximum))
print("%d"%(inputlist.index(maximum)+1),end="")