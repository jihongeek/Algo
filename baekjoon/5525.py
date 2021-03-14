from sys import stdin
import re
n = int(stdin.readline().strip())
length = int(stdin.readline().strip())
string = stdin.readline().strip()
count = 0

pattern = "(I(OI){%d,})"%n
for i in re.finditer(pattern,string):
    start,end = i.span()
    count += ((end-start)//2) - n + 1
print(count)