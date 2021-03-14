import sys

n,m = map(int,input().split())
paper = [ list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]

minos = [
    # (y,x)
    [(0,0),(0,1),(1,0),(1,1)], # ㅁ

    [(0,0),(0,1),(0,2),(0,3)], # |
    [(0,0),(1,0),(2,0),(3,0)], # -

    [(0,0),(1,0),(2,0),(2,1)], # L과 이로 만들어지는 경우들 
    [(1,0),(1,1),(1,2),(0,2)],
    [(0,0),(0,1),(1,1),(2,1)],
    [(0,0),(0,1),(0,2),(1,0)],
    [(2,0),(2,1),(1,1),(0,1)],
    [(0,0),(0,1),(0,2),(1,2)],
    [(0,0),(1,0),(2,0),(0,1)],
    [(0,0),(1,0),(1,1),(1,2)],

    [(0,0),(1,0),(1,1),(2,1)],# ㄹ과 이로 만들어지는 경우들
    [(1,0),(1,1),(0,1),(0,2)],
    [(0,0),(0,1),(1,1),(1,2)],
    [(2,0),(1,0),(1,1),(0,1)],

    [(0,0),(0,1),(0,2),(1,1)],# ㅜ
    [(0,0),(1,0),(2,0),(1,1)],# ㅏ
    [(1,0),(1,1),(1,2),(0,1)],# ㅗ
    [(1,0),(0,1),(1,1),(2,1)] # ㅓ 

]
maximum = 0
for mino in minos:
    for i in range(n):
       for j in range(m):
           sumOfBlocks = 0
           isInvalid = False
           if isInvalid == True:
               break
           for k in range(4):
               if mino[k][0]+i < n and mino[k][1]+j < m:
                   sumOfBlocks = sumOfBlocks + paper[mino[k][0]+i][mino[k][1]+j]
               else:
                   sumOfBlocks = 0
                   isInvalid = True
                   break
           if sumOfBlocks > maximum:
               maximum = sumOfBlocks
print(maximum)