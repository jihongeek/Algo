from sys import stdin

testcase = int(stdin.readline().strip())
for i in range(testcase):
    count = 0
    n,m = map(int,stdin.readline().strip().split())
    for b in range(1,n):
        for a in range(1,b):
            formula = (a**2+b**2+m)/(a*b)
            if formula - int(formula) == float(0):
                count+=1
    print(count)
