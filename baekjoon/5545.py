numOfTopp = int(input())
doughPrice,toppPrice = map(int,input().split())
doughCal = int(input())

toppCals = []
best = doughCal // doughPrice
for i in range(numOfTopp):
    toppCals.append(int(input()))
toppCals = sorted(toppCals, reverse=True)

for i in range(numOfTopp):
    calPerWon = (doughCal + sum(toppCals[:i+1])) // (doughPrice + toppPrice * (i+1)) 
    best = max(best,calPerWon)

print(best)
