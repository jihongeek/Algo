import sys 

numDict = {
    1 : 0,
    0 : 0,
    -1 : 0,
}
def checkPaper(n,xStart,xEnd,yStart,yEnd):
    for i in range(yStart,yEnd):
        for j in range(xStart+1,xEnd):
            if paper1[i][j] != paper1[i][j-1]:
                return -2
    for i in range(yStart+1,yEnd):
        for j in range(xStart,xEnd):
            if paper1[i][j] != paper1[i-1][j]:
                return -2
    return paper1[yStart][xStart]


def papercut(n,xStart,xEnd,yStart,yEnd):
    isSame = checkPaper(n,xStart,xEnd,yStart,yEnd)
    if n == 1:
        numDict[isSame] = numDict[isSame] + 1
        return
    elif isSame  != -2:
        numDict[isSame] = numDict[isSame] + 1
        return
    else:
        papercut(int(n/3), xStart, xStart + int(n/3), yStart, yStart + int(n/3))
        papercut(int(n/3), xStart + int(n/3), xStart + int(n/3) + int(n/3), yStart,yStart + int(n/3))
        papercut(int(n/3), xStart + int(n/3) + int(n/3), xStart + n, yStart,yStart + int(n/3))

        papercut(int(n/3), xStart, xStart + int(n/3), yStart + int(n/3), yStart + int(n/3) + int(n/3))
        papercut(int(n/3), xStart + int(n/3), xStart + int(n/3) + int(n/3), yStart + int(n/3), yStart + int(n/3) + int(n/3))
        papercut(int(n/3), xStart + int(n/3) + int(n/3), xStart + n, yStart + int(n/3), yStart + int(n/3) + int(n/3))

        papercut(int(n/3), xStart, xStart + int(n/3), yStart + int(n/3) + int(n/3), yStart + n)
        papercut(int(n/3), xStart + int(n/3), xStart + int(n/3) + int(n/3), yStart + int(n/3) + int(n/3), yStart + n)
        papercut(int(n/3), xStart + int(n/3) + int(n/3), xStart + n, yStart + int(n/3) + int(n/3), yStart + n)
 

n = int(input())
paper1 = [ list(map(int,sys.stdin.readline().strip().split())) for y in range(n)]
papercut(n,0,n,0,n)

print(numDict[-1])
print(numDict[0])
print(numDict[1])

