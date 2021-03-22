from sys import stdin 

n = int(stdin.readline().strip())
pictures = []
for i in range(n):
    pictures.append([stdin.readline().strip() for _ in range(5)])
mostSimilar = {
    'num' : (1,2),
    'similarity' : 0
}
for picture1 in range(n):
    for picture2 in range(n):
        if picture1 == picture2:
            continue
        count = 0
        for i in range(5):
            for j in range(7):
                if pictures[picture1][i][j] == pictures[picture2][i][j]:
                    count += 1
        if count > mostSimilar['similarity']:
            mostSimilar['similarity'] = count
            mostSimilar['num'] = (picture1+1,picture2+1)
for i in sorted(mostSimilar['num']):
    print(i)
