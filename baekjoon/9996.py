from sys import stdin 
import re
n = int(stdin.readline().strip())
pattern = re.sub("\*",".*",stdin.readline().strip())
for i in range(n):
    if re.fullmatch(pattern,stdin.readline().strip()):
        print("DA")
    else:
        print("NE")