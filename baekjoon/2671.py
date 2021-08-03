from sys import stdin 
import re

if re.fullmatch("(100+1+|01)+",stdin.readline().strip()):
    print("SUBMARINE")
else:
    print("NOISE")