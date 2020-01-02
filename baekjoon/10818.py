num = input()
inputlist = input().split()
minimum = int(inputlist[0])
maximum = int(inputlist[0])
for i in inputlist:
    if int(i) < minimum:
        minimum = int(i)
    elif int(i) > maximum:
        maximum = int(i)
print("%d %d"%(minimum,maximum),end="")