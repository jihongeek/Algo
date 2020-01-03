casenum = int(input())
for i in range(casenum):
    case = input()
    scorelist = []
    for j in case.split("X"):
        if len(j) == 0:
            pass
        else:
            scorelist.append(sum(list(range(1,len(j)+1))))
    print(sum(scorelist))
        