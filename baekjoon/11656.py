from sys import stdin
inputStr = stdin.readline().strip()
print("\n".join(sorted([inputStr[x:] for x in range(len(inputStr))])))

