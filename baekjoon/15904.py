from sys import stdin
import re

if re.search("U.*C.*P.*C.*",stdin.readline().strip()):
    print("I love UCPC")
else:
    print("I hate UCPC")