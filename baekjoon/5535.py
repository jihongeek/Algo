from sys import stdin

n = int(stdin.readline().strip())
for _ in  range(n):
    expressionList = stdin.readline().strip().split()
    num = float(expressionList[0])
    for operator in expressionList[1:]:
        if operator == "@":
            num *= 3
        elif operator == "%":
            num += 5 
        else:
            num -= 7
    print("%.2f"%num)