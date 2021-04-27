from sys import stdin

n,b = stdin.readline().strip().split()
b = int(b)
decimalN = 0
for i in range(len(n)-1,-1,-1):
    if 'A' <= n[i] <= 'Z':
        decimalN = decimalN + (10 + ord(n[i]) - ord('A')) * b**(len(n)-1 - i)
    else:
        decimalN = decimalN + int(n[i]) * b**(len(n) -1 -i)
print(decimalN)
