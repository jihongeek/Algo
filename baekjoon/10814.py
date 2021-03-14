import sys 

inputnum = int(sys.stdin.readline().strip())
peoples = {}
for i in range(inputnum):
    inputstrs = sys.stdin.readline().strip().split()
    age = int(inputstrs[0])
    name = inputstrs[1]
    if age in peoples:
        peoples[age].append(name)
    else:
        peoples[age] = [name]
agelist = sorted(list(peoples.keys()))

for i in agelist:
    for j in peoples[i]:
        print("%d %s"%(i,j))
