n = int(input())
papers = sorted(list(map(int, input().split())))
maxcitation = max(papers)
qindex = 0
for i in range(maxcitation+1):
    kCitation = 0 
    nminuskCitation = 0 
    for j in papers:
        if j >= i:
            kCitation+=1
        else:
            nminuskCitation+=1
    if kCitation >= i and nminuskCitation <= i:
        qindex = i
print(qindex)
