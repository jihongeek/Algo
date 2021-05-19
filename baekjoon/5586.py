from sys import stdin

inputStr = stdin.readline().strip()
ioi = 0
joi = 0
for i in range(len(inputStr)-3+1):
    if inputStr[i] + inputStr[i+1] + inputStr[i+2] == "IOI":
       ioi += 1 
    elif inputStr[i] + inputStr[i+1] + inputStr[i+2] == "JOI":
       joi += 1 
print(f"{joi}\n{ioi}")
