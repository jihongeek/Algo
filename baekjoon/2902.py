from sys import stdin
import re

algoname = stdin.readline().strip()
algoname_short = "".join(re.findall("[A-Z]",algoname))

print(algoname_short)