from sys import stdin 

n = int(stdin.readline().strip())
lines = [tuple(map(int,stdin.readline().strip().split())) for _ in range(n)]
lastEnd = lines[0][1] 
linesLength =lines[0][1] - lines[0][0] 
for line in lines[1:]:
    nowStart,nowEnd = line
    if lastEnd > nowStart:
        if lastEnd >= nowEnd:
            continue
        linesLength += (nowEnd - lastEnd)
    else:
        linesLength += (nowEnd - nowStart) 
    lastEnd = max(nowEnd,lastEnd)
print(linesLength)
