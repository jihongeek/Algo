from sys import stdin

height = 10
plates = stdin.readline().strip()
for i in range(1,len(plates)):
    if plates[i-1] == plates[i]:
        height += 5
    else:
        height += 10
print(height)
