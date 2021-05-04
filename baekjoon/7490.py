from sys import stdin 
import re
def findCase(nowIndex,nowEx):
    global n
    if nowIndex == len(series)-1:
        result = 0
        Ex = "".join(nowEx.split())
        operands = re.findall("[1-9]{1,}",Ex)
        operators = re.findall("[+-]",Ex)
        result = int(operands[0])
        operands = operands[1:] 
        for i in range(len(operands)):
            result = result + int(operators[i]+operands[i])
        if result == 0:
            print(nowEx)
        return
    findCase(nowIndex+1, nowEx +" "+series[nowIndex+1])
    findCase(nowIndex+1, nowEx +"+"+series[nowIndex+1])
    findCase(nowIndex+1, nowEx +"-"+series[nowIndex+1])
testcase = int(stdin.readline().strip())
for i in range(testcase):
    n = int(stdin.readline().strip())
    series = ""
    for j in range(1,n+1):
        series = series + str(j)
    findCase(0,series[0])
    print()
    