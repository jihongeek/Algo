diallist = ["0","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ","0"]
timelist = []
for i in input():
    for j in diallist:
        if i in j:
            timelist.append(diallist.index(j)+2)
print(sum(timelist))