import sys
# 리스트 합을 사용해서 연산자 계산하기 (-, +, 합치기)
def findUgly(lastCalc,secondIndex):
    global count
    if secondIndex == len(inputStr):
        number = int(lastCalc[0])
        for i in range(1,len(lastCalc),2):
            if lastCalc[i] == '+':
                number = number + int(lastCalc[i+1])
            else:
                number = number - int(lastCalc[i+1])
        for i in [2,3,5,7]:
            if number % i == 0:
                count = count + 1
                break
        return
    else:
        findUgly(lastCalc[:-1] + [lastCalc[-1] + inputStr[secondIndex]],secondIndex+1)
        findUgly(lastCalc + ['+'] + [inputStr[secondIndex]],secondIndex+1)
        findUgly(lastCalc + ['-'] + [inputStr[secondIndex]],secondIndex+1)

testcase = int(input())
for i in range(testcase):
    count = 0
    inputStr = list(sys.stdin.readline().strip())
    findUgly([inputStr[0]],1)
    print("Case #%d: %d"%(i+1,count))