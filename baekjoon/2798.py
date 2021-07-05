from sys import stdin 
n,m = map(int,stdin.readline().strip().split())
cards = list(map(int,stdin.readline().strip().split()))
maxOfUnderM = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if  maxOfUnderM < cards[i] + cards[j] + cards[k] <= m:
                maxOfUnderM =cards[i] + cards[j] + cards[k] 
print(maxOfUnderM)