from sys import stdin
count = 0
for i,char in enumerate(stdin.readline().strip()):
    if ord("A") <= ord(char) <= ord("Z") and (count+i)%4 != 0:
        count += (4-((count+i)%4))
print(count)
