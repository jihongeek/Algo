from sys import stdin 

count = 0
n = int(stdin.readline().strip())
k = 0  
for i,bit in enumerate(stdin.readline().strip()):
    if bit == "1":
        count += 1
print(count)