from sys import stdin
import re
testcase = int(stdin.readline().strip())

for i in range(testcase):
    radioCode = stdin.readline().strip()
    if re.fullmatch("(100+1+|01)+",radioCode):
        print("YES")
    else:
        print("NO")
    
