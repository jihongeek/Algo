"""
product of (cases of cloths(including no cloth)) but not naked!

"""

import sys 

testcase = int(input())
for testcase in range(testcase):
    clothTypes = [] 
    clothsDict = dict()
    n = int(input())
    for i in range(n):
        inputstr = sys.stdin.readline().strip().split()
        clothName = inputstr[0]
        clothType = inputstr[1]
        if clothType in clothsDict:
            clothsDict[clothType] = clothsDict[clothType] + 1
        else:
            clothTypes.append(clothType)
            clothsDict[clothType] = 0
            clothsDict[clothType] = clothsDict[clothType] + 1
    combinations = 1
    for i in clothTypes:
        combinations = combinations * (clothsDict[i] + 1)
    print(combinations - 1)