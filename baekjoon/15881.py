from sys import stdin 
n = int(stdin.readline().strip())
objects = stdin.readline().strip() 
count = 0
i = 0
while i <= n - 4:
    if objects[i:i+4] == "pPAp":
        count += 1
        i+=4
    else:
        i+=1
print(count)