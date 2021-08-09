from sys import stdin

code = stdin.read().strip()
while "BUG" in code:
    code = code.replace("BUG","")
print(code)