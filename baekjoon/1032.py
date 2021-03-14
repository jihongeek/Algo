import sys

n = int(sys.stdin.readline().strip())
count = 0
patern = ""
while 1:
    if count == 0:
        patern = sys.stdin.readline().strip()
    elif count == n:
        break
    else:
        filename = sys.stdin.readline().strip() 
        for i in range(len(filename)):
            if patern[i] != filename[i]:
                patern = patern[:i] + "?" + patern[i+1:]
    count = count + 1
print(patern)