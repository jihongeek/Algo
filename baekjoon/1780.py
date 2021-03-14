import sys 
numDict = {
    1 : 0,
    0 : 0,
    -1 : 0,
}
def checkPaper(n,paper):
    for i in range(len(paper)):
        for j in range(1,len(paper[0])):
            if paper[i][j] != paper[i][j-1]:
                return -2
    for i in range(1,len(paper)):
        for j in range(len(paper[0])):
            if paper[i][j] != paper[i-1][j]:
                return -2
    return paper[0][0]
def papercut(n,paper):
    isSame = checkPaper(n,paper)
    if n == 1:
        numDict[isSame] = numDict[isSame] + 1
        return
    elif isSame  != -2:
        numDict[isSame] = numDict[isSame] + 1
        return
    else:
        papercut(int(n/3),[paper[y][:int(n/3)] for y in range(int(n/3))])
        papercut(int(n/3),[paper[y][int(n/3):int(n/3)+int(n/3)] for y in range(int(n/3))])
        papercut(int(n/3),[paper[y][int(n/3)+int(n/3):] for y in range(int(n/3))])
        papercut(int(n/3),[paper[y][:int(n/3)] for y in range(int(n/3),int(n/3)+int(n/3))])
        papercut(int(n/3),[paper[y][int(n/3):int(n/3)+int(n/3)] for y in range(int(n/3),int(n/3)+int(n/3))])
        papercut(int(n/3),[paper[y][int(n/3)+int(n/3):] for y in range(int(n/3),int(n/3)+int(n/3))])
        papercut(int(n/3),[paper[y][:int(n/3)] for y in range(int(n/3)+int(n/3),n)])
        papercut(int(n/3),[paper[y][int(n/3):int(n/3)+int(n/3)] for y in range(int(n/3)+int(n/3),n)])
        papercut(int(n/3),[paper[y][int(n/3)+int(n/3):] for y in range(int(n/3)+int(n/3),n)])

n = int(input())
paper1 = [ list(map(int,sys.stdin.readline().strip().split())) for y in range(n)]
papercut(n,paper1)

print(numDict[-1])
print(numDict[0])
print(numDict[1])
