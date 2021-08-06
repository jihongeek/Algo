from sys import stdin

t = int(stdin.readline().strip())
a = t//300
b = (t%300)//60
c = t%300%60//10

if t%300%60%10 ==0:
    print(f"{a} {b} {c}")
else:
    print(-1)