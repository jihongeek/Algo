import sys
dots = {}
arrow = []
n = int(input())
for i in range(n):
    inputlist = sys.stdin.readline().strip().split()
    color = int(inputlist[1])
    location = int(inputlist[0])
    if color in dots:
        dots[color].append(location)
    else: 
        dots[color] = [location]

for color in dots:
    dots[color] = sorted(list(set(dots[color])))
    for index,location in enumerate(dots[color]):
        if index == 0:
            arrow.append(abs(location-dots[color][1]))
        elif index == len(dots[color]) - 1:
            arrow.append(abs(location-dots[color][-2]))
        else:
            first = abs(location - dots[color][index+1])
            second = abs(location - dots[color][index-1])  
            if first < second:
                arrow.append(first)
            else:
                arrow.append(second)
print(sum(arrow))