from sys import stdin

blue = 0
white = 0
def devide(rowStart,rowEnd,colStart,colEnd,n):
    global paper,blue,white
    allWhite = [['0']*(colEnd-colStart+1) for _ in range(rowEnd-rowStart+1)]
    allBlue = [['1']*(colEnd-colStart+1) for _ in range(rowEnd-rowStart+1)]
    devided = [paper[i][colStart:colEnd+1] for i in range(rowStart,rowEnd+1)] 
    if devided != allBlue and devided != allWhite:
        devide(rowStart, rowEnd - int(n/2), colStart, colEnd - int(n/2), int(n/2))
        devide(rowStart, rowEnd - int(n/2), colStart+int(n/2), colEnd, int(n/2))
        devide(rowStart + int(n/2), rowEnd, colStart+int(n/2), colEnd, int(n/2))
        devide(rowStart + int(n/2), rowEnd, colStart, colEnd - int(n/2), int(n/2))
    elif devided == allBlue:
        blue += 1
    elif devided == allWhite:
        white += 1
    return

        


n = int(stdin.readline().strip())
paper = [ stdin.readline().strip().split() for _ in range(n) ]
devide(0,n-1,0,n-1,n)
print(white)
print(blue)
