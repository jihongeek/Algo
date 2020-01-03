casenum = int(input())
for i in range(casenum):
    case = list(map(int,input().split()))
    mean = sum(case[1:])/case[0]
    great = []
    for i in case[1:]:
        if i > mean:
            great.append(i)
    print(str(format(len(great)/len(case[1:]),"10.3%")).strip())
