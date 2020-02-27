import re
p = re.compile("c=|c-|dz=|d-|lj|nj|s=|z=")
result = p.sub(" ",input())
print(len(result))
