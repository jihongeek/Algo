casenum = int(input())
for i in range(casenum):
    outputlist = []
    case = input()
    for i in case[2:]:
        outputlist.append(i*int(case[0]))
    print("".join(outputlist))
    